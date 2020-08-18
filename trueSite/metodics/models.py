from django.db import models



class MetodPage(models.Model):
    title = models.TextField(max_length=300)
    text_file = models.FileField(upload_to='metod/')
<<<<<<< HEAD
    objects = models.Manager()
=======
>>>>>>> 65f6722cdc04da11cd40413f298e3d2e7b267558


    def __str__(self):
        return self.title