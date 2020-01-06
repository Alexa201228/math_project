from django.shortcuts import render

from .models import MathPage

def math(request):
    mathtasks = MathPage.objects
    return render(request,'math/mathematics.html', {'math_tasks': mathtasks})

