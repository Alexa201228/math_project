from django.urls import path

from . import views

urlpatterns = [
    path('', views.metod, name="metod"),
    path('search/', views.metod_search, name='metod_search'),
    
]