# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Service,SubService,Features

# Register your models here.

# Ajustamos los campos editables y de lectura en el acceso del Super Usuario


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class SubServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class FeaturesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Por ultimo se registran en el Admin los
admin.site.register(Service, ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(Features, FeaturesAdmin)
