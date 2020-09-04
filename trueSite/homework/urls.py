from django.urls import path
from django.contrib.sitemaps.views import sitemap
from homework.sitemaps import HomeworkSitemap
from . import views

sitemaps = {
    'homeworks': HomeworkSitemap,
}

urlpatterns = [
    path('', views.homeworks, name="homework"),
    path('<int:task_id>/', views.taskDetails, name='task'),
]