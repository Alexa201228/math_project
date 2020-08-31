from django.shortcuts import render, get_object_or_404

from .models import SchoolPage

def schoolMath(request):
    tasks = SchoolPage.objects.all().order_by('title')
    return render(request, 'School/mainSchoolPage.html', {'tasks': tasks})

def category(request, theme):
    math_theme = SchoolPage.objects.filter(slug=theme)
    all_themes = SchoolPage.objects.all()
    return render(request, 'School/category.html', {'tasks': math_theme, 'themes': all_themes})

# Create your views here.
