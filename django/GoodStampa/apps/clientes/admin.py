from django.contrib import admin
from .models import CategoriaCliente, Cliente

# Register your models here.

admin.site.register(Cliente)
admin.site.register(CategoriaCliente)