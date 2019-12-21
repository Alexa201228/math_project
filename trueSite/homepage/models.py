from django.db import models

class HomePage(models.Model):
    image = models.ImageField(upload_to='home_images/')
    description = models.CharField(max_length=300)
