from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

# import models
from .models import Prueba ##Importamos Prueba de la carpeta modelos
#ListView la importamos para procesos de listado.
from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView): 
    template_name = "home/lista.html"
    queryset = ['1', '10', '20','30']
    context_object_name = 'ListaNumeros'
    
class ListaPrueba(ListView): 
    template_name = "home/lista_prueba.html"
    model = Prueba ## A que tabla vamos a hacer referencia para listar
    context_object_name = 'Lista' ##Siempre hace falta un context object name

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'

class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"
