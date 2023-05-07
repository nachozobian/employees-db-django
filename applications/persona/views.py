from pdb import post_mortem
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, TemplateView, UpdateView, DeleteView

from .models import Empleado
# Create your views here.

#1
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    
    #Para hacer una paginacion tenemos que indicar el tamaño de bloque en el que queremos paginar
    paginate_by = 4
    ordering = 'first_name'
    
    def get_queryset(self): 
        print("***********************************")
        palabra_clave = self.request.GET.get("kword", '')
        #Jorge => J, full_name__icontains busca algun nombre que contenga la cadena, en este caso la cadena es vacía
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    ordering = 'first_name'
    context_object_name = 'empleados'
    #Para hacer una paginacion tenemos que indicar el tamaño de bloque en el que queremos paginar
    paginate_by = 10
    model = Empleado

    
#2  
class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        #El codigo que yo quiera
        area = self.kwargs['shor_name']
        lista = Empleado.objects.filter(departamento__name = area)
        return lista

#3
class ListByJobEmpleados(ListView):
    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        job = self.kwargs['job']
        lista = Empleado.objects.filter(job = job)
        return lista
#4
class ListEmpleadosByKword(ListView):
    """lista empleado por palabra clave"""
    template_name = 'persona/by_kword.html'
    conext_object_name = 'empleados'

    def get_queryset(self): 
        print("***********************************")
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista
    
#5
class ListHabilidadesEmpleados(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        #El atributo habilidades es m2m
        palabra_clave = self.request.GET.get("kword", '')
        if palabra_clave == '':
            return []
        else:
            empleado = Empleado.objects.get(id = int(palabra_clave))
            return empleado.habilidades.all()
#1.- Lista todos los empleados de la empresa
#2.- Listar todos los empleados que pertenecen a un área de la empresa.
#3.- Listar empleados por trabajo.
#4.- Listar todos los empleados por palabra clave.
#5.- Listar habilidades de un empleado.

#La vista genérica detailed view permite ver mejor los datos de una entrada de la tabla.


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #Todo un proceso
        context['titulo'] = 'empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]            #('__all__') era para todos los atributos
                         #Que atributos del modelo queremos que se muestren en pantalla. Cuantos campos son necesarios para un empleado?
                         #Crea un registro.
    #Nos falta agregar un boton para guardar los datos incluidos en la base de datos, eso se hace con un POST en CreateView, se hace practicamente igual
    #Que en el GET
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        print(empleado)
        return super(EmpleadoCreateView, self).form_valid(form)

 
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs): #No se han validado previamente los datos.
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form): #Una vez se han validado los datos
        #logica del proceso
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


class InicioView(TemplateView):
    #Vista que carga la pagina views
    template_name = 'inicio.html'