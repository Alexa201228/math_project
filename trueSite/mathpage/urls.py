from django.urls import path

from . import views

urlpatterns = [
    path('', views.math, name="math"),
    path('razvitie-ponyatya-o-chisle.html/', views.tasks_per_theme, name="thematic_tasks"),
]