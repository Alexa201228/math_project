from django.urls import path

from . import views

urlpatterns = [
    path('', views.math, name="math"),
    path('<slug:theme>/', views.categoryTheme, name='category'),
    path(r'^theme-autocomplete/$', views.ThemeAutocomplete.as_view(model=Theme, create_field='theme'), name='theme-autocomplete',),
]