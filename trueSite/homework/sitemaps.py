from django.contrib.sitemaps import Sitemap
from .models import homework

class HomeworkSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return homework.objects.all()

    def lastmod(self, obj):
        return obj.created
