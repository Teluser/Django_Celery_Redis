import time
from celery import shared_task


@shared_task()
def waiting_seconds(i):
    time.sleep(5)
    print(f"Finish task {i}")