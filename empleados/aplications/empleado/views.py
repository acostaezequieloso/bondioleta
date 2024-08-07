from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import Empleado

class IndexView (TemplateView):
    template_name= 'empleado/home.html'

class pruebalistview (ListView):
    template_name= 'empleado/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):

    model = Empleado
    template_name = 'empleado/lista-prueba.html'
    context_object_name = 'lista_prueba'



