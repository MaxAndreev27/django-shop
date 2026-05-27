#!/bin/sh

set -e

echo "==> Running database migrations on persistent volume..."
python manage.py migrate --noinput

echo "==> Starting Celery worker in background..."
celery -A config worker --loglevel=info &

echo "==> Starting Flower monitor on port 5555..."
celery -A config flower --port=5555 --address=0.0.0.0 &

echo "==> Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:8000 --workers 2 config.wsgi