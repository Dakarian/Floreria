from django.shortcuts import render
from .models import Flores
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def galeria(request):
    flowers = Flores.objects.all()  # select * from pelicula
    return render(request, 'core/galeria.html', {'listaflores': flowers})

def login(request):
    return render(request,'core/login.html')

def quienes_somos(request):
    return render(request,'core/quienes_somos.html')

def carrito(request):
    lista = request.session.get("carro", "")
    arr = lista.split(";")
    return render(request, "core/carrito.html", {'lista': arr})

def anadir_carro(request, id):
    #recuperar valor de la pelicula
    #clausula "select * from Pelicula where name like (%id%)"
    flowers=Flores.objects.filter(name__contains=id)
    valor=Flores.valor
    # recuperar una sesion llamada 'carro', de no existir no deja nada ''
    sesion = request.session.get("carro", "")
    # buscar la pelicula en el interior del listado
    arr = sesion.split(";")
    # almacena los registros limpios
    arr2 = ''
    sw = 0
    cant = 1
    for f in arr:
        flr = f.split(":")
        if flr[0] == id:
            cant = int(flr[1])+1
            sw = 1
            arr2 = arr2+str(flr[0])+":"+str(cant)+":"+str(valor)+";"
        elif not flr[0]=="":
            cant=flr[1]
            arr2 = arr2+str(flr[0])+":"+str(cant)+str(valor)+";"
    # pregunta si la pelicula existe o no
    if sw == 0:
        arr2 = arr2+str(id)+":"+str(1)+str(valor)+";"

    # en la session 'carro' almaceno lo que trae la sesion mas el titulo de la pelicula
    request.session["carro"] = arr2
    # recuperar el listado de peliculas
    flowers = Flores.objects.all()
    # renderizar la pagina, pasandole el listado de peliculas
    msg = 'agrego flor'
    return render(request, 'core/galeria.html', {'listaflores': flowers, 'msg': msg})

def vaciar_carrito(request):
    request.session["carro"] = ""
    lista = request.session.get("carro", "")
    return render(request, "core/carrito.html", {'lista': lista})

def eliminar_flor(request, id):
    mensaje = ''
    flr = Flores.objects.get(name=id)
    try:
        flr.delete()
        mensaje = 'elimino flor'
    except:
        mensaje = 'no pudo eliminar la flor'

    flr = Flores.objects.all()
    return render(request, 'core/galeria.html', {'listaflores': flr, 'msg': mensaje})