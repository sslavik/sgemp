from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nomProveedor = models.TextField()
    direccion = models.TextField()
    nif = models.CharField(max_length=9)
    telefono = models.TextField()
    telefono2 = models.TextField()
    email = models.TextField()
    web = models.TextField()
    