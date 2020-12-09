from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import MathPage

def math(request):
    mathtasks = MathPage.objects.all()
    paginator = Paginator(mathtasks, 10)
    page = request.GET.get('page')
    try:
        exercise = paginator.page(page)
    except PageNotAnInteger:
        exercise = paginator.page(1)
    except EmptyPage:
        exercise = paginator.page(paginator.num_pages)
    
    return render(request, 'math/mathematics.html', {'page': page, 'mathtasks': list(set(exercise))})

def categoryTheme(request, theme):
    math_theme = MathPage.objects.filter(slug=theme)
    all_themes = MathPage.objects.all()
    paginator = Paginator(math_theme, 10)
    page = request.GET.get('page')
    try:
        math_thema = paginator.page(page)
    except PageNotAnInteger:
        math_thema = paginator.page(1)
    except EmptyPage:
        math_thema = paginator.page(paginator.num_pages)
    return render(request, 'math/categories.html', {'page': page, 'math_tasks': math_thema, 'themes': list(set(all_themes))})
    
