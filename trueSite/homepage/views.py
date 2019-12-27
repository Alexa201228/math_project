from django.shortcuts import render

from .models import HomePage

def Home(request):
    home = HomePage.objects
    return render(request,'homepage/home.html', {'home': home})
