from django.db import models

from mathpage import views

class HomePage(models.Model):
    image = models.ImageField(upload_to='home_images/')
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category