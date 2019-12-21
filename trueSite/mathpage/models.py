from django.db import models

class MathPage(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='math_images/')
    little_summary = models.CharField(max_length=300)
