from django.db import models
from django.urls import reverse


class SchoolPage(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    theme = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='school_images/', blank=True, null=True)
    description = models.TextField(blank=True, default='')
    fileSolution = models.FileField(blank=True, upload_to='school_materials/')
    slug = models.SlugField(max_length=250, default='')
    image_solution = models.ImageField(upload_to='school_images/', blank=True, null=True)
    video_source = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title + " " + self.theme

    def get_absolute_url(self):
        return reverse('category', args=[self.theme, self.slug])

# Create your models here.
