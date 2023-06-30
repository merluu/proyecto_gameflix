from django.shortcuts import render
from .models import Juego
from .forms import JuegoForm
from .forms import CustomUserForm
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

def register(request):
    data = {
        'form' : CustomUserForm()
    }
    return render(request,'registration/register.html',data)

def login(request):
    return render(request,'aplicacion/login.html')

def nuevo_juego(request):
    data = {
        'form' : JuegoForm() 
    }
    return render(request,'aplicacion/nuevo_juego.html',data)

def juego_inicio(request):
    juegos = Juego.objects.all()
    data = {
        'juegos': juegos
    }
    return render(request,'aplicacion/juego_inicio.html',data)

