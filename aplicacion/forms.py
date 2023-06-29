from django import forms
from django.forms import ModelForm
from .models import Juego
from .models import Cliente

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
        if len(nombre)<4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre
    

    def va_precio(self):
        precio =self.cleaned_data.get('precio')
        if precio<=0:
            raise forms.ValidationError("El precio tiene que ser mayor que 0")
        return precio
    
    
class ClienteForm (ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut','pnombre','snombre','papellido','sapellido','fecha_nacimiento','email']