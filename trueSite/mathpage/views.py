from django.shortcuts import render, get_object_or_404

from .models import MathPage

def math(request):
    mathtasks = MathPage.objects.all()
    return render(request, 'math/mathematics.html', {'mathtasks': mathtasks})

def categoryTheme(request, theme):
    math_theme = MathPage.objects.filter(slug=theme)
    all_themes = MathPage.objects.all()
    return render(request, 'math/categories.html', {'math_tasks': math_theme, 'themes': all_themes})
    
