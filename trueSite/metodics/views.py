from django.shortcuts import render, get_object_or_404
from .models import MetodPage

def metod(request):
    metods = MetodPage.objects
    return render(request, 'metodics/metod.html', {'metods': metods})
