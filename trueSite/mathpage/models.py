from django.db import models

class MathPage(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    theme = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='math_images/', blank=True, default=None, null=True)
    description = models.TextField(blank=True, default='')
    solution = models.TextField(blank=True, default='')
    image_solution = models.ImageField(upload_to='math_images/', blank=True, default=None, null=True)

    def __str__(self):
        return self.title + " " + self.theme
    
    
