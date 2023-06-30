from django import forms
from django.forms import ModelForm
from .models import Juego
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto
from .models import opciones_consultas
from .models import Cliente
from django.contrib.auth.models import User

class JuegoForm(ModelForm):
    id = forms.CharField(widget=forms.TextInput)
    nombre = forms.CharField(widget=forms.TextInput)
    precio = forms.CharField(widget=forms.TextInput)
    descripcion = forms.CharField(widget=forms.TextInput)
    fecha_creacion = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'precio', 'descripcion', 'fecha_creacion']

    def val_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre
    
    def va_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio tiene que ser mayor que 0")
        return precio

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
    rut = forms.CharField(widget=forms.TextInput)
    pnombre = forms.CharField(widget=forms.TextInput)
    snombre = forms.CharField(widget=forms.TextInput)
    papellido = forms.CharField(widget=forms.TextInput)
    sapellido = forms.CharField(widget=forms.TextInput)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.CharField(widget=forms.EmailInput())
    usrdjango = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Cliente
        fields = ['rut', 'pnombre', 'snombre', 'papellido', 'sapellido', 'fecha_nacimiento', 'email', 'usrdjango']

    def clean_pnombre(self):
        pnombre = self.cleaned_data.get('pnombre')
        if len(pnombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return pnombre

    def clean_papellido(self):
        papellido = self.cleaned_data.get('papellido')
        if len(papellido) < 4:
            raise forms.ValidationError("El apellido debe tener al menos 4 caracteres")
        return papellido
