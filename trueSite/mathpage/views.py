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
    def get_create_option(self, context, q):
        """Form the correct create_option to append to results."""
        create_option = []
        display_create_option = False
        if self.create_field and q:
            page_obj = context.get('page_obj', None)
            if page_obj is None or page_obj.number == 1:
                display_create_option = True

            # Don't offer to create a new option if a
            # case-insensitive) identical one already exists
            existing_options = (self.get_result_label(result).lower()
                                for result in context['object_list'])
            if q.lower() in existing_options:
                display_create_option = False

        if display_create_option and self.has_add_permission(self.request):
            create_option = [{
                'id': q,
                'text': _('Create "%(new_value)s"') % {'new_value': q},
                'create_id': True,
            }]
        return create_option

def math(request):
    mathtasks = MathPage.objects.all()
    return render(request, 'math/mathematics.html', {'mathtasks': mathtasks})

def categoryTheme(request, theme):
    math_theme = MathPage.objects.filter(slug=theme)
    all_themes = MathPage.objects.all()
    return render(request, 'math/categories.html', {'math_tasks': math_theme, 'themes': all_themes})
    
