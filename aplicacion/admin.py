from django.contrib import admin
from .models import Juego , Cliente , Carrito , DetalleCarrito , Venta 
# Register your models here.

admin.site.register(Juego)
admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(DetalleCarrito)
admin.site.register(Venta)

