from django.contrib.sitemaps import Sitemap
from .models import MetodPage

class MetodSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return MetodPage.objects.all()

    def location(self, item):
        return '/metodics/' + item.title