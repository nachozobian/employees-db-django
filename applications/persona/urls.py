from django.contrib import admin
from django.urls import path
from . import views



app_name = "persona_app"

urlpatterns = [
    path('',views.InicioView.as_view(), name= 'inicio'),
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    
    path('listar-by-area/<shor_name>/',
         views.ListByAreaEmpleados.as_view(),
         name='empleados_area'),

    path('listar_by_job/<job>/', views.ListByJobEmpleados.as_view()),
    path('buscar_empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar_habilidades_empleado/', views.ListHabilidadesEmpleados.as_view()),  

    path('ver_empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),

    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'), #Create View.
    
    path('lista_empleados_admin/', views.ListEmpleadosAdmin.as_view(), name='empleados_admin'),
    path(
        'success/', 
        views.SuccessView.as_view(),
        name='correcto'
        ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
        ), 
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
        ), 
]