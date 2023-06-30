from os import name
from django.urls import path
from.views import home,contacto,cartelera, juego1, juego2, juego3, juego4, juego5,juego6,juego7,juego8,indexadmin ,listado_clientes,modificar_cliente,eliminar_cliente, register, login,nuevo_cliente,listado_juegos,modificar_juego,eliminar_juego,nuevoo_juegoo

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
    path('register/', register,name="register"),
    path('login/', login,name="login"),
    path('indexadmin/', indexadmin,name="indexadmin" ),
    path ('listado-clientes/',listado_clientes,name ="listado_clientes"),
    
    path('modificar-cliente/<rut>/',modificar_cliente,name="modificar_cliente"),
    path('eliminar-cliente/<rut>/',eliminar_cliente,name="eliminar_cliente"),
    path ('nuevo-cliente/',nuevo_cliente,name="nuevo_cliente"),

##JUEGOS
    path ('listado-juegos/',listado_juegos,name ="listado_juegos"),
    path('modificar-juego/<id>/',modificar_juego,name="modificar_juego"),
    path('eliminar-juego/<id>/',eliminar_juego,name="eliminar_juego"),
    path('nuevoo-juegoo/',nuevoo_juegoo,name="nuevoo_juegoo"),
    

]