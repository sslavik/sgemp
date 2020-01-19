from django.contrib import admin
from .models import Service

# Register your models here.

# Ajustamos los campos editables y de lectura en el acceso del Super Usuario


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Por ultimo se registran en el Admin los 
admin.site.register(Service, ServiceAdmin)
