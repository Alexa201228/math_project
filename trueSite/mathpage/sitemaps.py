from django.contrib.sitemaps import Sitemap
from .models import MathPage
from django.urls import reverse

class MathSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return ['trueSite']

    def location(self, item):
        return reverse(item)