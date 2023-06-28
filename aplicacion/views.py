from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'aplicacion/home.html')

def contacto(request):
    return render(request,'aplicacion/contacto.html')

def cartelera(request):
    return render(request,'aplicacion/cartelera.html')

def juego5(request):
    return render(request,'aplicacion/juego5.html')

def juego6(request):
    return render(request,'aplicacion/juego6.html')

def juego7(request):
    return render(request,'aplicacion/juego7.html')

def juego8(request):
    return render(request,'aplicacion/juego8.html')





