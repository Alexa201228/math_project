from django.contrib.sitemaps import Sitemap
from .models import MathPage
from django.urls import reverse
from mathpage.urls import urlpatterns as mathPatterns

class MathSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        obj = []
        for pattern in mathPatterns:
            obj.append(pattern.name)
        return obj


    def location(self, item):
        return reverse(item)