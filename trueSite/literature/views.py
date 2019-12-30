from django.shortcuts import render

from .models import Literature

def Litera(request):
    lit = Literature.objects
    return render(request, 'literature/litera.html', {'lit': lit})

