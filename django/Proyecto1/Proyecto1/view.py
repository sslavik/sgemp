from django.http import HttpResponse
from django.shortcuts import render
from Proyecto1.models.persona import Persona


def listaPersonas(request):
    p1 = Persona("Jose Carlos", "Soler", 21, "Marketing")
    p2 = Persona("Sergio", "Montel", 22, "RRHH")
    p3 = Persona("Ismael", "Carrasco", 21, "Administración")
    p4 = Persona("Pablo", "Torres", 24, "Producción")

    personas = [p1,p2,p3,p4]

    return render(request, "personas.html", {"personas": personas})
