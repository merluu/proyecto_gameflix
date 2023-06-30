from django import forms
from django.forms import ModelForm
from .models import Juego
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto
from .models import opciones_consultas
from .models import Cliente
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput)
    correo = forms.CharField(widget=forms.TextInput)
    tipo_consulta = forms.ChoiceField(choices=opciones_consultas, widget=forms.Select(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Contacto
        #fields = ("nombre","correo","tipo_consulta","mensaje")
        fields = '__all__' 

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['rut','pnombre','snombre','papellido','sapellido','fecha_nacimiento','email','usrdjango']
        

##juegos crud
class JuegoForm(ModelForm):

    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'precio', 'descripcion', 'fecha_creacion']

