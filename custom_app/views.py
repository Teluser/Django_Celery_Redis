from django.shortcuts import render
from django.shortcuts import HttpResponse
import time


def task(request):
    time.sleep(10)
    return HttpResponse("The task is run successfully!")
