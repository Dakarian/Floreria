#urls de la pagina
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria',galeria,name='GALE'),
    path('quienes_somos',quienes_somos,name='QUIEN'),
    path('login',login,name='LOGIN'),
    path('carrito',carrito,name='SHOP'),
    path('agregar_carro/<id>/',anadir_carro,name='ANADIR_CARRO'),
    path('vaciar_carrito',vaciar_carrito,name="VACIARCARRITO"),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR'),
    path('registro',registro,name='REGISTRO'),
    path('login_ingresar',login_ingresar,name='LOGIN_INGRESAR'),
    path('logout',cerrar_sesion,name='LOGOUT'),

]
