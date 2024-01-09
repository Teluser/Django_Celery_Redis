import os
from celery import Celery
from celery.signals import setup_logging
from logging.config import dictConfig
from django.conf import settings


@setup_logging.connect
def config_loggers(*args, **kwargs):
    dictConfig(settings.LOGGING)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
