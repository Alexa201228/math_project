from django.db import models



class MetodPage(models.Model):
    title = models.TextField(max_length=300)
    text_file = models.FileField(upload_to='metod/')
    objects = models.Manager()
    description = models.ImageField(blank=True, null=True, upload_to='metod_images/')


    def __str__(self):
        return self.title
