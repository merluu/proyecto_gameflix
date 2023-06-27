from django.urls import path
from.views import home,contacto,cartelera

urlpatterns = [
    path('', home,name="home" ),
    path('contacto/', contacto,name="contacto" ),
    path('cartelera/', cartelera,name="cartelera" ),
]