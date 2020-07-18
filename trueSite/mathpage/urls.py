from django.urls import path

from . import views

urlpatterns = [
    path('', views.math, name="math"),
    path('<slug:theme>/', views.category_theme, name='category')
]