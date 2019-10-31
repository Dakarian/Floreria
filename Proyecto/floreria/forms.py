from django import forms
from django.forms import ModelForm
from .models import Flores

class FlorForm(ModelForm):

    class Meta:
        model = Flores
        fields = ['name','foto','descripcion','valor','stock']