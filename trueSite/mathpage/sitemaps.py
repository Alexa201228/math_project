from django.contrib.sitemaps import Sitemap
from .models import MathPage
from django.core.urlresolvers import reverse

class MathSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return MathPage.objects.all()

    def location(self, item):
        return reverse(item)