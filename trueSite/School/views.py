from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import SchoolPage

def schoolMath(request):
    tasks = SchoolPage.objects.all().order_by('title')
    themes = SchoolPage.objects.all().distinct('theme')
    paginator = Paginator(tasks, 10)
    page = request.GET.get('page')
    try:
        task = paginator.page(page)
    except PageNotAnInteger:
        task = paginator.page(1)
    except EmptyPage:
        task = paginator.page(paginator.num_pages)
    return render(request, 'School/mainSchoolPage.html', {'page': page, 'tasks': task, 'themes': themes})

def category(request, theme):
    math_theme = SchoolPage.objects.filter(slug=theme)
    all_themes = SchoolPage.objects.all()
    paginator = Paginator(math_theme, 10)
    page = request.GET.get('page')
    try:
        math_thema = paginator.page(page)
    except PageNotAnInteger:
        math_thema = paginator.page(1)
    except EmptyPage:
        math_thema = paginator.page(paginator.num_pages)
    return render(request, 'School/category.html', {'page': page, 'tasks': math_thema, 'themes': all_themes})

# Create your views here.
