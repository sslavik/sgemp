from django.urls import path
from .views import index, uno

urlpatterns = [
    path('', index),
    path('uno/', uno)
]
