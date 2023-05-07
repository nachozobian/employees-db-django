from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name', #Full name no existe en el modelo pero para que funcione necesitamos darle una fucnion.
        'avatar',
        'id',   #Que le asigne algun valor.
    )
    def full_name (self, obj):
        return obj.first_name + ' ' +  obj.last_name
    
    search_fields = ('first_name',) #Integramos un buscador por nombre al modelo de DJango.
    list_filter = ('job','habilidades','departamento') # Filtro en funcion de los contadores.
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)

