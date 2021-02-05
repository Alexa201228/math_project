from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import SchoolPage

def schoolMath(request, theme=None):
    category = None
    tasks = SchoolPage.objects.all().order_by('title')
    themes = SchoolPage.objects.all().distinct('theme')
    for i in themes:
        i = ' '.join(str(i).split())
    paginator = Paginator(tasks, 10)
    page = request.GET.get('page')
    if theme:
        category = SchoolPage.objects.filter(slug=theme)[0]
        tasks = tasks.filter(slug=theme)
        paginator = Paginator(tasks, 10)
        page = request.GET.get('page')
    try:
        task = paginator.page(page)
    except PageNotAnInteger:
        task = paginator.page(1)
    except EmptyPage:
        task = paginator.page(paginator.num_pages)
    return render(request, 'School/category.html', {'page': page, 'tasks': task, 'themes': themes, 'category': category})

