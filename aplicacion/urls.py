from django.urls import path
from.views import (home,
contacto,
cartelera, 
juego1, 
juego2, 
juego3, 
juego4, 
juego5,
juego6,
juego7,
juego8,
nuevo_juego,
juego_inicio,listado_clientes,modificar_cliente,eliminar_cliente)

urlpatterns = [
    path('', home,name="home" ),
    path('contacto/', contacto,name="contacto" ),
    path('cartelera/', cartelera,name="cartelera" ),
    path('juego1/', juego1,name="juego1" ),
    path('juego2/', juego2,name="juego2" ),
    path('juego3/', juego3,name="juego3" ),
    path('juego4/', juego4,name="juego4" ),
    path('juego5/', juego5,name="juego5" ),
    path('juego6/', juego6,name="juego6" ),
    path('juego7/', juego7,name="juego7" ),
    path('juego8/', juego8,name="juego8" ),

    
    path('juego_inicio/', juego_inicio,name="juego_inicio" ),

    path ('listado-clientes/',listado_clientes,name ="listado_clientes"),

    path('nuevo-juego/', nuevo_juego,name="nuevo_juego"),

    #path('nuevo-cliente/',nuevo_cliente,name="nuevo_cliente"),
    
    path('modificar-cliente/<rut>/',modificar_cliente,name="modificar_cliente"),

    path('eliminar-cliente/<rut>/',eliminar_cliente,name="eliminar_cliente"),
]