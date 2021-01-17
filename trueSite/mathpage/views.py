from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import MathPage

def math(request, theme=None):
    category = None
    mathtasks = MathPage.objects.all()
    mathThemes = MathPage.objects.all().distinct('theme')
    paginator = Paginator(mathtasks, 10)
    page = request.GET.get('page')
    if theme:
        category = MathPage.objects.filter(slug=theme)[0]
        mathtasks = mathtasks.filter(slug=theme)
        paginator = Paginator(mathtasks, 10)
        page = request.GET.get('page')
    try:
        exercise = paginator.page(page)
    except PageNotAnInteger:
        exercise = paginator.page(1)
    except EmptyPage:
        exercise = paginator.page(paginator.num_pages)
    
    return render(request, 'math/categories.html', {'page': page, 'mathtasks': exercise, 'math_themes': mathThemes, 'category': category })

# def categoryTheme(request, theme):
#     math_theme = MathPage.objects.filter(slug=theme)
#     all_themes = MathPage.objects.all().distinct('theme')
#     paginator = Paginator(math_theme, 10)
#     page = request.GET.get('page')
#     try:
#         math_thema = paginator.page(page)
#     except PageNotAnInteger:
#         math_thema = paginator.page(1)
#     except EmptyPage:
#         math_thema = paginator.page(paginator.num_pages)
#     return render(request, 'math/categories.html', {'page': page, 'math_tasks': math_thema, 'themes': all_themes})
    
