from django.db import models

class homework(models.Model):
    title = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='homework_images', null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
