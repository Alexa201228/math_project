from django.shortcuts import render, get_object_or_404
from .models import StudentsWorks
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def students(request):
    studworks = StudentsWorks.objects.all()
    paginator = Paginator(studworks, 10)
    page = request.GET.get('page')
    try:
        studw = paginator.page(page)
    except PageNotAnInteger:
        studw = paginator.page(1)
    except EmptyPage:
        studw = paginator.page(paginator.num_pages)
    return render(request, 'students/works.html', {'page': page,'studworks': studw})
