from django.db import models
import os

class Literature(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='literature_images', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
