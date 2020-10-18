from django.contrib.sitemaps import Sitemap
from .models import SchoolPage

class SchoolSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return SchoolPage.objects.all()

    def location(self, item):
        return '/School/' + item.slug