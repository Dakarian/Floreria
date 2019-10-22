from django.db import models

# Create your models here.
class Flores(models.Model):
    name=models.CharField(max_length=100, primary_key=True)
    foto=models.ImageField(upload_to="flor",null=False)
    descripcion=models.TextField(max_length=300, null=False)
    valor=models.IntegerField(null=False)
    stock=models.IntegerField(null=False)
    
    def __str__(self):
        return self.name