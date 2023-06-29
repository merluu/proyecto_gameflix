from django.shortcuts import render
from .models import Cliente
from .models import Juego

# Create your views here.

def home(request):
    return render(request,'aplicacion/home.html')

def contacto(request):
    return render(request,'aplicacion/contacto.html')

def cartelera(request):
    return render(request,'aplicacion/cartelera.html')

def juego1(request):
    return render(request,'aplicacion/juego1.html')

def juego2(request):
    return render(request,'aplicacion/juego2.html')

def juego3(request):
    return render(request,'aplicacion/juego3.html')

def juego4(request):
    return render(request,'aplicacion/juego4.html')

def juego5(request):
    return render(request,'aplicacion/juego5.html')

def juego6(request):
    return render(request,'aplicacion/juego6.html')

def juego7(request):
    return render(request,'aplicacion/juego7.html')

def juego8(request):
    return render(request,'aplicacion/juego8.html')

def listaCliente(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes': clientes
    }
    return render(request,'aplicacion/listaCliente.html',data)


def juego_inicio(request):
    juegos = Juego.objects.all()
    data = {
        'juegos': juegos
    }
    return render(request,'aplicacion/juego_inicio.html',data)
