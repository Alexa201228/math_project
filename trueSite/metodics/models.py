from django.db import models



class MetodPage(models.Model):
    title = models.TextField(max_length=300)
    text_file = models.FileField(upload_to='metod/')
    objects = models.Manager()
<<<<<<< HEAD

=======
>>>>>>> f15ca1ede7f01b541aba9bfd8e479203263b739a

    def __str__(self):
        return self.title
