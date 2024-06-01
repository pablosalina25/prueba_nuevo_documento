from django.db import models

class CSVFile(models.Model):
    file = models.FileField(upload_to='csvs/')

    def __str__(self):
        return self.file.name
