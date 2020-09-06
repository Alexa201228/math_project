from django.db import models
from django.urls import reverse
from django.contrib.sitemaps import ping_google


class MathPage(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    theme = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='math_images/', blank=True, null=True)
    description = models.TextField(blank=True, default='')
    fileSolution = models.FileField(blank=True, upload_to='math_materials/')
    slug = models.SlugField(max_length=250, default='')
    image_solution = models.ImageField(upload_to='math_images/', blank=True, null=True)

    def __str__(self):
        return self.title + " " + self.theme

    
    def save(self):
        super(MathPage, self).save()
        try:
            ping_google()
        except Exception:
            pass
