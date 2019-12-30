from django.db import models
import os

class Literature(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='literature_images', null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.description[:100] +" ..."
    
    def little_title(self):
        return self.title[:50] + "..."