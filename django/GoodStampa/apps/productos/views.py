from django.shortcuts import render


def index(request):
    return render(request, 'productos/productos.html', {"navProducto" : "active"})
# Create your views here.
