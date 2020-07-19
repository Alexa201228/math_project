from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotInteger
from .models import MetodPage

def metod(request):
    metods = MetodPage.objects.all()
    paginator = Paginator(metods, 10)
    page = request.GET.get('page')
    try:
        metod = paginator.page(page)
    except PageNotInteger:
        metod = paginator.page(1)
    except EmptyPage:
        metod = paginator.page(paginator.num_pages)
    return render(request, 'metodics/metod.html', {'metods': metods, 'page': page})
