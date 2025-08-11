#!/usr/bin/env bash
set -euo pipefail

# Ensure working directory
cd /code || cd "$(dirname "$0")"

# Create static dir if missing (harmless if exists)
mkdir -p staticfiles
# Ensure media dir exists for uploads; respect MEDIA_ROOT if provided
MEDIA_DIR=${MEDIA_ROOT:-media}
mkdir -p "$MEDIA_DIR"

echo "Running database migrations..."
if command -v poetry >/dev/null 2>&1; then
  poetry run python manage.py migrate --noinput
else
  python manage.py migrate --noinput
fi

# Optionally set or update the superuser password from env
if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
  echo "Ensuring superuser ${DJANGO_SUPERUSER_USERNAME} exists and updating password..."
  if command -v poetry >/dev/null 2>&1; then
    poetry run python manage.py shell -c "from django.contrib.auth import get_user_model; import os; U=get_user_model(); u=os.environ.get('DJANGO_SUPERUSER_USERNAME'); p=os.environ.get('DJANGO_SUPERUSER_PASSWORD'); e=os.environ.get('DJANGO_SUPERUSER_EMAIL',''); obj,created=U.objects.get_or_create(username=u, defaults={'email': e, 'is_superuser': True, 'is_staff': True}); obj.is_superuser=True; obj.is_staff=True; obj.set_password(p); obj.save(); print('superuser', u, 'created' if created else 'updated')"
  else
    python manage.py shell -c "from django.contrib.auth import get_user_model; import os; U=get_user_model(); u=os.environ.get('DJANGO_SUPERUSER_USERNAME'); p=os.environ.get('DJANGO_SUPERUSER_PASSWORD'); e=os.environ.get('DJANGO_SUPERUSER_EMAIL',''); obj,created=U.objects.get_or_create(username=u, defaults={'email': e, 'is_superuser': True, 'is_staff': True}); obj.is_superuser=True; obj.is_staff=True; obj.set_password(p); obj.save(); print('superuser', u, 'created' if created else 'updated')"
  fi
fi

# Optionally seed initial data when DB is empty
if [ "${SEED_FIXTURES:-0}" = "1" ]; then
  echo "Seeding fixtures if empty..."
  if command -v poetry >/dev/null 2>&1; then
    poetry run python - <<'PY'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blog_project.settings')
import django
django.setup()
from posts.models import Post
from django.core.management import call_command
if Post.objects.exists():
    print('Posts exist; skipping seed')
else:
    print('Loading posts/fixtures/seed.json...')
    call_command('loaddata','posts/fixtures/seed.json')
PY
  else
    python - <<'PY'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blog_project.settings')
import django
django.setup()
from posts.models import Post
from django.core.management import call_command
if Post.objects.exists():
    print('Posts exist; skipping seed')
else:
    print('Loading posts/fixtures/seed.json...')
    call_command('loaddata','posts/fixtures/seed.json')
PY
  fi
fi

echo "Starting Gunicorn..."
if command -v poetry >/dev/null 2>&1; then
  exec poetry run gunicorn blog_project.wsgi:application --bind 0.0.0.0:"${PORT:-8000}"
else
  exec gunicorn blog_project.wsgi:application --bind 0.0.0.0:"${PORT:-8000}"
fi
