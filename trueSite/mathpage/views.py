from django.shortcuts import render

from .models import MathPage

def math(request):
    mathtasks = MathPage.objects
    return render(request,'math/mathematics.html', {'math_tasks': mathtasks})

def tasks_per_theme(request):
    tasks = MathPage.objects.filter(theme='Развитие понятия о числе')
    return render(request,'math/razvitie-ponyatya-o-chisle.html', {'tasks': tasks})

