#urls de la pagina
from django.contrib import admin
from django.urls import path,include
from .views import home, galeria, quienes_somos,login,carrito

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria',galeria,name='GALE'),
    path('quienes_somos',quienes_somos,name='QUIEN'),
    path('login',login,name='LOGIN'),
    path('carrito',carrito,name='SHOP'),
]
