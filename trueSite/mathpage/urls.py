from django.urls import path

from . import views

urlpatterns = [
    path('', views.math, name="math"),
    path('<str:theme_name>/', views.tasks_per_theme, name="thematic_tasks"),
]