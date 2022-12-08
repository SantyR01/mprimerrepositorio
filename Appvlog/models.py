from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre=models.CharField(max_length=40)
    año_de_publicacion=models.DateField()
    genero=models.CharField(max_length=10)
    

class Autor(models.Model):
    nombre_autor=models.CharField(max_length=20)
    año_de_nacimiento=models.DateField()
    email=models.EmailField()
    pais=models.CharField(max_length=10)
    
class Sucursal(models.Model):
    nombre=models.CharField(max_length=15)
    codigo_postal=models.IntegerField()
    ciudad=models.CharField(max_length=10)
    numero_de_sucursal=models.IntegerField()