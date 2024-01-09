import time
from celery import shared_task


@shared_task()
def waiting_seconds(i):
    time.sleep(180)
    print(f"Finish task {i}")