from django.shortcuts import render, get_object_or_404
from .models import StudentsWorks

def students(request):
    studworks = StudentsWorks.objects
    return render(request, 'students/works.html', {'studworks': studworks})
