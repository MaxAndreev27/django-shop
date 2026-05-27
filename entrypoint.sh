#!/bin/sh

set -e

echo "==> Running database migrations on persistent volume..."
python manage.py migrate --noinput

echo "==> Starting Celery worker in background..."
celery -A config worker --loglevel=info &

echo "==> Starting Gunicorn server..."
exec gunicorn --bind :8000 --workers 2 config.wsgi