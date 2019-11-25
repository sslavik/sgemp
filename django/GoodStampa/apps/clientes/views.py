from django.shortcuts import render
from django.http import HttpResponse
from apps.clientes.models import Cliente
from apps.clientes.models import CategoriaCliente


# Create your views here.


def index(request):

    clientes = Cliente.objects.all()

    return render(request, "clientes/clientes.html", {"clientes": clientes, "navCliente" : "active"})
