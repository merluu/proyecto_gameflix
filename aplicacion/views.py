from django.shortcuts import render
from .models import Juego
from .forms import JuegoForm
from .forms import ContactoForm
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

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto enviado"
        else:
            data["form"] = formulario
    return render(request,'aplicacion/contacto.html',data)

def indexadmin(request):
    return render(request,'aplicacion/indexadmin.html')

