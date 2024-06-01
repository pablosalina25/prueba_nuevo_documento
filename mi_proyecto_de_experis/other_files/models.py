from django.db import models

# Create your models here.

class Archivo(models.Model):
    archivo = models.FileField(upload_to='archivos/')

