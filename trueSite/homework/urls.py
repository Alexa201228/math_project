from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeworks, name="homework"),
    path('<int:task_id>/', views.task_details, name='task'),
]