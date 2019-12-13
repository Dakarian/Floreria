from rest_framework import serializers
from .models import Flores

class FloresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flores
        fields = ['name','foto','descripcion','valor','stock']