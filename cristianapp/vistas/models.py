from django.db import models

# Create your models here.
class libros(models.Model):
    libro_id = models.CharField(max_length=60)
    Nombre = models.CharField(max_length=60)
    editorial = models.CharField(max_length=60)
    año = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20)