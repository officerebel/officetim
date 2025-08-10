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

echo "Starting Gunicorn..."
if command -v poetry >/dev/null 2>&1; then
  exec poetry run gunicorn blog_project.wsgi:application --bind 0.0.0.0:"${PORT:-8000}"
else
  exec gunicorn blog_project.wsgi:application --bind 0.0.0.0:"${PORT:-8000}"
fi
