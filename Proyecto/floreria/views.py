from django.shortcuts import render, redirect
from .models import Flores
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .forms import FlorForm, CustomUserForm, elemento

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def galeria(request):
    flowers = Flores.objects.all()  # select * from pelicula
    return render(request, 'core/galeria.html', {'listaflores': flowers})

def login(request):
    return render(request,'registration/login.html')
    
def adm(request):
    return render(request,'/admin')

def quienes_somos(request):
    return render(request,'core/quienes_somos.html')

@login_required(login_url='/login')
def carrito(request):
    lista=request.session["carritox"]
    suma=0
    for item in lista:
        suma=suma+int(item["total"])           
    return render(request,'core/carrito.html',{'lista':lista,'total':suma})

def anadir_carro(request, id):
    f=Flores.objects.get(name=id)
    lista=request.session["carritox"]
    el=elemento(f.name,f.valor,1)
    sw=0
    suma=0
    clon=[]
    for item in lista:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(el.toString())
    lista=clon    
    request.session["carritox"]=lista
    flowers=Flores.objects.all()    
    return render(request,'core/galeria.html',{'listaflores':flowers,'total':suma})

def vaciar_carrito(request):
    request.session["carritox"] = ""
    lista = request.session.get("carro", "")
    return render(request, "core/carrito.html", {'lista': lista})

@permission_required('floreria.delete_flores')
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

def registro(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)      
            request.session["carritox"] = []
            request.session["carrito"] = []
            auth_login(request, user)
            return redirect(to='HOME')

    return render(request, 'registration/registro.html', data)

def login_ingresar(request):
    if request.POST:
        u = request.POST.get("txtUsuario")
        p = request.POST.get("txtPass")
        usu = authenticate(request, username=u, password=p)        
        request.session["carritox"] = []
        request.session["carrito"] = []
        if usu is not None and usu.is_active:
            auth_login(request, usu)
            return render(request, 'core/home.html')
    return render(request, 'registration/login.html')

@login_required(login_url='/login')
def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>alert('cerro sesion');window.location.href='/';</script>")

@permission_required('floreria.add_flores')
def ingreso_flor(request):
    data = {
        'form':FlorForm()
    }
    if request.method == 'POST':
        formulario = FlorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['msj'] = "Almacenado correctamente"
        data['form'] = formulario

    return render(request, 'core/ingreso_flor.html', data)

@permission_required('floreria.change_flores')
def modificar_flor(request, id):
    flor = Flores.objects.get(name=id)
    data = {
        'form':FlorForm(instance=flor)
    }
    if request.method == 'POST':
        formulario = FlorForm(data=request.POST, instance=flor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['msj'] = "Modificado correctamente"
        data['form'] = formulario
    return render(request, 'core/modificar_flor.html', data)