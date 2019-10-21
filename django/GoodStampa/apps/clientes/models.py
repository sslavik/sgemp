from django.db import models

# Create your models here.


class CategoriaCliente(models.Model):
    AUTONOMO = 'A'
    SOCIEDAD = 'S'
    PARTICULAR = 'P'

    CATEGORIA = [
        (AUTONOMO, 'Autonomo'),
        (SOCIEDAD, 'Sociedad'),
        (PARTICULAR, 'Particular')
    ]

    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIA,
        default=PARTICULAR,
    )


class Cliente(models.Model):
    nomCliente = models.TextField()
    direccion = models.TextField()
    nif = models.CharField(max_length=9)
    telefono = models.TextField()
    telefono2 = models.TextField()
    email = models.TextField()
    web = models.TextField()
    categoriaCliente = models.ForeignKey(
        'CategoriaCliente',
        on_delete=models.CASCADE,
    )
