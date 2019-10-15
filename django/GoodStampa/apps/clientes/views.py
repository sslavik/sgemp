from django.shortcuts import render
from django.http import HttpResponse
from GoodStampa.models.cliente import Cliente

# Create your views here.


def index(request):

    p1 = Cliente("Jose Carlos", "Soler", 21, "Marketing")
    p2 = Cliente("Sergio", "Montel", 22, "RRHH")
    p3 = Cliente("Ismael", "Carrasco", 21, "Administración")
    p4 = Cliente("Pablo", "Torres", 24, "Producción")

    clientes = [p1, p2, p3, p4]

    return render(request, "clientes/clientes.html", {"clientes": clientes})
