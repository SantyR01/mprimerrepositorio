from django import forms

    
class Autorformulario(forms.Form):
    nombre_autor=forms.CharField(max_length=20)
    año_de_nacimiento=forms.DateField()
    email=forms.EmailField()
    pais=forms.CharField(max_length=10)

class Libroformulario(forms.Form):
    nombre_=forms.CharField(max_length=20)
    año_de_publicacion=forms.DateField()
    genero=forms.CharField(max_length=10)

class Sucursalformulario(forms.Form):
    nombre=forms.CharField(max_length=15)
    codigo_postal=forms.IntegerField()
    ciudad=forms.CharField(max_length=10)
    numero_de_sucursal=forms.IntegerField()