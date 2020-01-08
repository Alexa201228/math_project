from django.shortcuts import render

from .models import MathPage

def math(request):
    mathtasks = MathPage.objects.distinct()
    return render(request,'math/mathematics.html', {'math_tasks': mathtasks})

def tasks_per_theme(request, theme_name):
    tasks = MathPage.objects.filter(theme=theme_name)
    return render(request,'math/thematic_tasks.html', {'tasks': tasks})

