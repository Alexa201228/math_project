from django.shortcuts import render

from .models import homework

def homeworks(request):
    homew = homework.objects
    return render(request, 'homework/homework.html', {'homew': homew})


