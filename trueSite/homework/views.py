from django.shortcuts import render, get_object_or_404
from .models import homework

from .models import homework

def homeworks(request):
    homew = homework.objects
    return render(request, 'homework/homework.html', {'homew': homew})

def task_details(request, task_id):
    task_det = get_object_or_404(homework,pk=task_id)
    return render(request, 'homework/task.html', {'task': task_det})


