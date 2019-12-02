from django.contrib import admin
# Importamos el modelo usado para los proyectos
from .models import Project

# Register your models here.

# Lo registramos en el fichero
admin.site.register(Project)
