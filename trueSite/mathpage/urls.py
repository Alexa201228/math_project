from django.urls import path

from . import views

urlpatterns = [
    path('', views.math, name="math"),
    path('<slug:slug>/', views.category_theme, name='category')
]