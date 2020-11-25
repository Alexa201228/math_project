from django.db import models

class StudentsWorks(models.Model):
    presentation = models.FileField(upload_to='presentations/', blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    source = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.presentation)[14:]

    def title(self):
        if self.name:
            return self.name
        else:
            return str(self.presentation)[14:len(str(self.presentation)) - 5]

