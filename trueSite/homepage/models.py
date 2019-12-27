from django.db import models

class HomePage(models.Model):
    image = models.ImageField(upload_to='home_images/')
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.category
