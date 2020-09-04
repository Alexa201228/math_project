from django.contrib.sitemaps import Sitemap
from .models import MathPage

class MathSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return MathPage.objects.all()