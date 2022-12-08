from django.shortcuts import render
from django.http import HttpResponse

from Appvlog.models import Autor
from Appvlog.models import Libro
from Appvlog.models import Sucursal

from django.core import serializers

from Appvlog.forms import  Autorformulario
from Appvlog.forms import  Libroformulario
from Appvlog.forms import  Sucursalformulario

# Create your views here.

def inicio(request):
    
   return render(request,"Appvlog/inicio.html")


def autor (request):
    if request.method == "POST":
            miFormulario = Autorformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.data
                  print(informacion)
                  
                  autor = Autor (nombre_autor=informacion["nombre_autor"], año_de_nacimiento=informacion["año_de_nacimiento"],email=informacion["email"],pais=informacion["pais"],)
                  autor.save()
                  return render(request, "Appvlog/inicio.html")
    else:
        miFormulario = Autorformulario()
 
    return render (request, "Appvlog/autor.html", {"miFormulario": miFormulario})





def libro (request):
   return  HttpResponse("vista de libro")

def libro (request):
    if request.method == "POST":
            miFormulario_li = Libroformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario_li)
 
            if miFormulario_li.is_valid:
                  informacion = miFormulario_li.data
                  print(informacion)
                  
                  libro = Libro (nombre=informacion["nombre"], año_de_publicacion=informacion["año_de_publicacion"],genero=informacion["genero"],)
                  libro.save()
                  return render(request, "Appvlog/inicio.html")
    else:
        miFormulario_li = Libroformulario()
 
    return render (request, "Appvlog/libro.html", {"miFormulario_li": miFormulario_li})




def sucursal (request):
    return  HttpResponse("vista de sucursal")


def sucursal (request):
    if request.method == "POST":
            miFormulario_suc = Sucursalformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario_suc)
 
            if miFormulario_suc.is_valid:
                  informacion = miFormulario_suc.cleaned_data
                  print(informacion)
                  
                  sucursal = Sucursal (nombre=informacion["nombre"], codigo_postal=informacion["codigo_postal"],ciudad=informacion["ciudad"], numero_de_sucursal=informacion["numero_de_sucursal"],)
                  sucursal.save()
                  return render(request, "Appvlog/inicio.html")
    else:
        miFormulario_li = Sucursalformulario()
 
    return render (request, "Appvlog/sucursal.html", {"miFormulario_suc": miFormulario_suc})














def autorapi (request):
    Todos_los_autores=Autor.objects.all()
    return  HttpResponse(serializers.serialize("json", Todos_los_autores))


def libroapi (request):
    Todos_los_libros=Libro.objects.all()
    return  HttpResponse(serializers.serialize("json", Todos_los_libros))


def sucursalapi (request):
    Todas_las_sucursales=sucursal.objects.all()
    return  HttpResponse(serializers.serialize("json", Todas_las_sucursales))
