from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def galeria(request):
    return render(request,'core/galeria.html')

def login(request):
    return render(request,'core/login.html')

def quienes_somos(request):
    return render(request,'core/quienes_somos.html')

def carrito(request):
    return render(request,'core/carrito.html')