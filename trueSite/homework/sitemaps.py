from django.contrib.sitemaps import Sitemap
from .models import homework
from django.urls import reverse

class HomeworkSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return homework.objects.all()

    def location(self, item):
        return reverse(item)

