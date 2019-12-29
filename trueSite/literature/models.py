from django.db import models

class Literature(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='literature_images')
    books = models.FileField(upload_to='books', null=True)
    description = models.TextField()

    def __str__(self):
        return self.title