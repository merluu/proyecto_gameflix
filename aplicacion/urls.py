from django.urls import path
from.views import home,contacto,cartelera,juego5,juego6,juego7,juego8,listaCliente

urlpatterns = [
    path('', home,name="home" ),
    path('contacto/', contacto,name="contacto" ),
    path('cartelera/', cartelera,name="cartelera" ),
    path('juego5/', juego5,name="juego5" ),
    path('juego6/', juego6,name="juego6" ),
    path('juego7/', juego7,name="juego7" ),
    path('juego8/', juego8,name="juego8" ),
    path('listaCliente/', listaCliente,name="listaCliente" ),


]