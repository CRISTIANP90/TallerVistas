from django.shortcuts import render
from .models import libros

# Instanciamos las vistas genericas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

# Nos sirve para redireccionar despues de una accion revertiendo patrones
# De expresiones regulares

from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
# Habilitamos los mensajes para class-bassed views
from django.contrib.messages.views import SuccessMessageMixin
# Habilitamos los formularios en Django
from django import forms

class CrearLibro(SuccessMessageMixin,CreateView):
    model = libros
    form = libros
    fields = "__all__" 
    success_message = 'Libro Creado Correctamente !'
 
class ListarLibros(ListView):
    model = libros
 
class DetalleLibro(DetailView):
    model = libros
 
class ActualizacionesLibros(SuccessMessageMixin, UpdateView):
    model = libros
    form = libros
    field = "__all__"
    def get_success_url(self):
        return reverse('leer')
   
class EliminarLibro (SuccessMessageMixin, DeleteView):
    model = libros
    form = libros
    field = "__all__"
    def get_success_url(self):
        success_message = 'Libro Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')

