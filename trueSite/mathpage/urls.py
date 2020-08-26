from django.urls import path, re_path

from . import views
from .models import Theme

urlpatterns = [
    path('', views.math, name="math"),
    path('<slug:theme>/', views.categoryTheme, name='category'),
]