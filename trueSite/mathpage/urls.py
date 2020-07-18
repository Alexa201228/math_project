from django.urls import path

from . import views

urlpatterns = [
    path('', views.math, name="math"),
    path('<slug:slug>/', views.categoryTheme, name='category')
]