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