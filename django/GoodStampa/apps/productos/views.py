from django.shortcuts import render


def index(request):
    return render(request, 'productos/productos.html', None)
# Create your views here.
