from django.shortcuts import render

def math(request):
    return render(request,'math/mathematics.html')
