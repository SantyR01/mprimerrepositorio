from django.urls import path
from Appvlog import views

urlpatterns = [
   path('', views.inicio,name="Inicio"),
   path('autor/', views.autor, name="Autor"),
   path('autorapi/', views.autorapi),
   path('libroapi/', views.libroapi),
   path('libro/', views.libro,  name="Libro"),
   path('sucursal/', views.sucursal, name="Sucursal"),
   path('sucursalapi/', views.sucursalapi),
   



]