#!/usr/bin/env bash
set -euo pipefail

# Ensure working directory
cd /code || cd "$(dirname "$0")"

# Create static dir if missing (harmless if exists)
mkdir -p staticfiles

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

echo "Starting Gunicorn..."
if command -v poetry >/dev/null 2>&1; then
  exec poetry run gunicorn blog_project.wsgi:application --bind 0.0.0.0:"${PORT:-8000}"
else
  exec gunicorn blog_project.wsgi:application --bind 0.0.0.0:"${PORT:-8000}"
fi
