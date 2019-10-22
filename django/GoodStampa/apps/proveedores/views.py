from django.shortcuts import render


def index(request):

    return render(request, 'proveedores/proveedores.html', {"navProveedor" : "active"})
# Create your views here.


