from django.urls import path
from.views import home,contacto,cartelera, juego1, juego2, juego3, juego4

urlpatterns = [
    path('', home,name="home" ),
    path('contacto/', contacto,name="contacto" ),
    path('cartelera/', cartelera,name="cartelera" ),
    path('juego1/', juego1,name="juego1" ),
    path('juego2/', juego2,name="juego2" ),
    path('juego3/', juego3,name="juego3" ),
    path('juego4/', juego4,name="juego4" ),
]