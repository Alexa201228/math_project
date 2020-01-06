from django.db import models

class MathPage(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='math_images/', null=True)
    description = models.TextField(null=True)
    solution = models.TextField(null=True)
