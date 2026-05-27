import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
# Чистий префікс для налаштувань Celery в settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
