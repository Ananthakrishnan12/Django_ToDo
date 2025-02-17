from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Task


def add_task(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
