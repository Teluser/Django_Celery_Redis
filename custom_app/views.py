from django.shortcuts import HttpResponse
from .tasks import waiting_seconds

def task(request):
    for i in range(1, 10):
        waiting_seconds.delay(i)
    return HttpResponse("The task is run successfully!")
