from django.shortcuts import render, get_object_or_404

from .models import MathPage

def math(request):
    mathtasks = MathPage.objects.all()
    return render(request, 'math/mathematics.html', {'math_tasks': mathtasks})

def category_theme(request, theme):
    math_theme = get_object_or_404(MathPage, slug=theme)
    return render(request, 'math/categories.html', {'math_tasks': math_theme})
    

# def ponyatia_o_chisle(request):
#     tasks = MathPage.objects.filter(theme='Развитие понятия о числе')
#     return render(request,'math/razvitie-ponyatya-o-chisle.html', {'tasks': tasks})

# def korni(request):
#     tasks = MathPage.objects.filter(theme='Корни, степени и логарифмы')
#     return render(request,'math/korni-stepeni-logarifmi.html', {'tasks': tasks})

# def priamie(request):
#     tasks = MathPage.objects.filter(theme='Прямые и плоскости в пространстве')
#     return render(request,'math/priamie-i-ploskosti-v-prostranstve.html', {'tasks': tasks})

# def kombinatorica(request):
#     tasks = MathPage.objects.filter(theme='Элементы комбинаторики')
#     return render(request,'math/elementi-kombinatoriki.html', {'tasks': tasks})

# def coordinati(request):
#     tasks = MathPage.objects.filter(theme='Координаты и векторы')
#     return render(request,'math/coordinati-i-vectori.html', {'tasks': tasks})

# def trigonometria(request):
#     tasks = MathPage.objects.filter(theme='Основы тригонометрии')
#     return render(request,'math/osnovi-trigonometrii.html', {'tasks': tasks})

# def functions(request):
#     tasks = MathPage.objects.filter(theme='Функции, их свойства и графики')
#     return render(request,'math/functions-ich-grafiki-i-svoistva.html', {'tasks': tasks})

# def mnogogranniki(request):
#     tasks = MathPage.objects.filter(theme='Многогранники и круглые тела')
#     return render(request,'math/mnogogranniki-i-kruglie-tela.html', {'tasks': tasks})

# def matan(request):
#     tasks = MathPage.objects.filter(theme='Начала математического анализа')
#     return render(request,'math/nachala-matanaliza.html', {'tasks': tasks})

# def integral(request):
#     tasks = MathPage.objects.filter(theme='Интеграл и его применение')
#     return render(request,'math/integral-i-ego-primenenie.html', {'tasks': tasks})

# def teorver(request):
#     tasks = MathPage.objects.filter(theme='Элементы теории вероятностей и математической статистики')
#     return render(request,'math/elementi-teorii-veroyatnostey-i-matstat.html', {'tasks': tasks})

# def neravenstva(request):
#     tasks = MathPage.objects.filter(theme='Уравнения и неравенства')
#     return render(request,'math/uravnenia-i-neravenstva.html', {'tasks': tasks})

