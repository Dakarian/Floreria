from django import forms
from django.forms import ModelForm
from .models import Flores
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlorForm(ModelForm):

    name = forms.CharField(min_length=3, max_length=50)
    descripcion = forms.CharField(min_length=10,max_length=300)
    valor = forms.IntegerField(min_value=0,max_value=500000)
    stock = forms.IntegerField(min_value=0,max_value=99999)

    class Meta:
        model = Flores
        fields = ['name','foto','descripcion','valor','stock']


class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']


class elemento:
    nombre=""
    precio=0
    cantidad=0

    def __init__(self,nombre,precio,cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    
    def toString(self):
        return {
            'nombre': self.nombre,
            'precio': str(self.precio),
            'cantidad': str(self.cantidad),
            'total':str(self.total())
        }
    def total(self):
        return str(int(self.precio)*int(self.cantidad))