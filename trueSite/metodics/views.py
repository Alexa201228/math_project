from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MetodPage
from .forms import SearchForm
from django.contrib.postgres.search import TrigramSimilarity

def metod(request):
    metods = MetodPage.objects.all().order_by('title')
    paginator = Paginator(metods, 10)
    page = request.GET.get('page')
    try:
        metod = paginator.page(page)
    except PageNotAnInteger:
        metod = paginator.page(1)
    except EmptyPage:
        metod = paginator.page(paginator.num_pages)
    return render(request, 'metodics/metod.html', {'page': page, 'metods': metod})


def metod_search(request):
    form = SearchForm()
    query = None
    results = MetodPage.objects.all().order_by('title')
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = MetodPage.objects.annotate(similarity=TrigramSimilarity('title', query),).filter(similarity__gt=0.1).order_by('-similarity').order_by('title')
    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    try:
        metod = paginator.page(page)
    except PageNotAnInteger:
        metod = paginator.page(1)
    except EmptyPage:
        metod = paginator.page(paginator.num_pages)

    return render(request, 'metodics/search.html',
                    {
                    'results':metod})