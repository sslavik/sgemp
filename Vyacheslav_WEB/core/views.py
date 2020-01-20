from django.shortcuts import render, HttpResponse
from array import array
from services.models import Service

# Create your views here.

# def home(request):
#    return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")

# Renderiza la vista del template


def index(request):
    services = Service.objects.all()
    return render(request, "core/home.html", {'services': services})
