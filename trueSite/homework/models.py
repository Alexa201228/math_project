from django.db import models

class homework(models.Model):
    title = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='homework_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    homework_file = models.FileField(blank=True)


    def __str__(self):
        return self.title
