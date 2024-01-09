import time
from celery import shared_task
import logging

celery_log = logging.getLogger("celery.custom.log")

@shared_task()
def waiting_seconds(i):
    time.sleep(180)
    celery_log.debug(f"Finish task {i}")