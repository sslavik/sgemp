from django.http import HttpResponse
from django.shortcuts import render
from Proyecto1.models.persona import Persona


def listaPersonas(request):
    p1 = Persona("Persona 1", "Carrasco", 20, "Administración")

    personas = [p1]

    return render(request, "personas.html", {"personas": personas})
