from django.shortcuts import render, redirect
from .models import Cliente
from .models import Juego
from .forms import CustomUserForm
from .forms import ContactoForm
from .forms import ClienteForm
from .forms import JuegoForm
# Create your views here.


def home(request):
    return render(request, 'aplicacion/home.html')


def contacto(request):
    return render(request, 'aplicacion/contacto.html')


def cartelera(request):
    return render(request, 'aplicacion/cartelera.html')


def juego1(request):
    return render(request, 'aplicacion/juego1.html')


def juego2(request):
    return render(request, 'aplicacion/juego2.html')


def juego3(request):
    return render(request, 'aplicacion/juego3.html')


def juego4(request):
    return render(request, 'aplicacion/juego4.html')


def juego5(request):
    return render(request, 'aplicacion/juego5.html')


def juego6(request):
    return render(request, 'aplicacion/juego6.html')


def juego7(request):
    return render(request, 'aplicacion/juego7.html')


def juego8(request):
    return render(request, 'aplicacion/juego8.html')


def register(request):
    data = {
        'form': CustomUserForm()
    }
    return render(request, 'registration/register.html', data)


def login(request):
    return render(request, 'aplicacion/login.html')


def nuevo_juego(request):
    data = {
        'form': JuegoForm()
    }
    return render(request, 'aplicacion/nuevo_juego.html', data)



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
    return render(request, 'aplicacion/contacto.html', data)


def indexadmin(request):
    return render(request, 'aplicacion/indexadmin.html')

##lista cliente##


def listado_clientes(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes': clientes
    }
    return render(request, 'aplicacion/listado_clientes.html', data)

## nuevo cliente ##


def nuevo_cliente(request):
    data = {
        'form': ClienteForm()
    }

    if request.method=='POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado con exito"
        else:
            print(formulario.errors)
            
    return render(request, 'aplicacion/nuevo_cliente.html', data)


# modificar cliente
def modificar_cliente(request, rut):
    cliente = Cliente.objects.get(rut=rut)
    data = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "cliente modificado correctamente "
            data['form'] = formulario
    return render(request, 'aplicacion/modificar_cliente.html', data)


def eliminar_cliente(request, rut):
    cliente = Cliente.objects.get(rut=rut)
    cliente.delete()

    return redirect(to="listado_clientes")





## LISTA DE JUEGOS

def listado_juegos(request):
    juegos = Juego.objects.all()
    data = {
        'juegos': juegos
    }
    return render(request, 'aplicacion/listado_juegos.html', data)


def modificar_juego(request, id):
    juego = Juego.objects.get(id=id)
    data = {
        'form': JuegoForm(instance=juego)
    }

    if request.method == 'POST':
        formulario = JuegoForm(data=request.POST, instance=juego)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "juego modificado correctamente "
            data['form'] = formulario
    return render(request, 'aplicacion/modificar_juego.html', data)

def eliminar_juego(request, id):
    juego = Juego.objects.get(id=id)
    juego.delete()

    return redirect(to="listado_juegos")

def nuevoo_juegoo(request):
    data = {
        'form': JuegoForm()
    }

    if request.method=='POST':
        formulario = JuegoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado con exito"
        else:
            print(formulario.errors)
            
    return render(request, 'aplicacion/nuevoo_juegoo.html', data)