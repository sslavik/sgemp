from django.db import models

# Create your models here.

class CategoriaArticulo(models.Model):
    SILVER = 'S'
    GOLD = 'G'
    PLATINUM = 'P'

    CATEGORIA = [
        (SILVER, 'Plata'),
        (GOLD, 'Oro'),
        (PLATINUM, 'Platino')
    ]

    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIA,
        default=SILVER,
    )

class Articulo(models.Model):
    nomArticulo = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    referencia = models.CharField(max_length=9)
    CategoriaArticulo = models.ForeignKey(
        'CategoriaArticulo',
        on_delete=models.CASCADE,
    )
