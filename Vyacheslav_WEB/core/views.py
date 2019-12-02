from django.shortcuts import render, HttpResponse

# Create your views here.

# def home(request):
#    return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")

# Renderiza la vista del template


def index(request):
    return render(request, "core/home.html")
