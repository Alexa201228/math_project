from django.db import models

class StudentsWorks(models.Model):
    presentation = models.FileField(upload_to='presentations/')

    def __str__(self):
        return str(self.presentation)[14:]

    def title(self):
        return str(self.presentation)[14:]

