from django.shortcuts import render
from .models import Flores

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
    return render(request,'core/carrito.html')