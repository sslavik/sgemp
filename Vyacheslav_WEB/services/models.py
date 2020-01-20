from django.db import models

# Create your models here.


class SubService(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Nombre de Sub Servicio")
    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "subServicio"
        verbose_name_plural = "subServicios"
        ordering = ['name']

    def __str__(self):
        return self.name


class Features(models.Model):
    name = models.CharField(
        verbose_name="Nombre de Complemento", max_length=200)
    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "Complemento"
        verbose_name_plural = "Complementos"
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    subService = models.ManyToManyField(SubService)
    features = models.ManyToManyField(Features)
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.TimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.TimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title
