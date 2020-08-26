from django.shortcuts import render, get_object_or_404
from dal import autocomplete

from .models import MathPage

class ThemeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return MathPage.objects.none()
        qs = MathPage.objects.all()
        if self.q:
            qs = qs.filter(theme__istartswith=self.q)
        return qs

    def has_add_permission(self, request):
        return True
    def create_option(self, text):
        return self.get_queryset().get_or_create(theme=text)

def math(request):
    mathtasks = MathPage.objects.all()
    return render(request, 'math/mathematics.html', {'mathtasks': mathtasks})

def categoryTheme(request, theme):
    math_theme = MathPage.objects.filter(slug=theme)
    all_themes = MathPage.objects.all()
    return render(request, 'math/categories.html', {'math_tasks': math_theme, 'themes': all_themes})
    
