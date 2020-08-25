from django.db import models
from django.urls import reverse

class Themes(models.Model):
    theme = models.CharField(max_length=200, blank=True, null=True, default='')

class MathPage(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='math_images/', blank=True, null=True)
    description = models.TextField(blank=True, default='')
    solution = models.TextField(blank=True, default='')
    slug = models.SlugField(max_length=250, default='')
    image_solution = models.ImageField(upload_to='math_images/', blank=True, null=True)

    def __str__(self):
        return self.title + " " + self.theme

    def get_absolute_url(self):
        return reverse('categoryTheme', args=[self.theme, self.slug])
