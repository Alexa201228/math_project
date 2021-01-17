from django.urls import path

from . import views

urlpatterns = [
    path('', views.schoolMath, name="schoolMath"),
    path('<slug:theme>/', views.schoolMath, name='category'),
]