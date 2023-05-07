from django.db import models

# Create your models here.
class Departamento(models.Model): #Utilizamos la ORM de DJango

    #Los campos actuales son obligatorios. Para añadirlo basta con pasarle blank = True
    #Ejemplo:
    #name = models.CharField('Nombre', max_length=50, blank=True)
    #Cuando no siempre tome un valor podemos aplicar null=True.
    #Podemos querer que no se repita nunca, para ello unique=True
    #editable=False, no se puede acceder desde el administrador.
    name = models.CharField('Nombre', max_length=50)#No sobrepoblar la base de datos
    shor_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)#Este valor no

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ['name', 'shor_name']
        

    def __str__(self):
        return str(self.id) + self.name + '-' + self.shor_name
#DJango entiende que los id vienen por defecto en la base de datos y no hace falta declarar
#el atributo id. Internamente lo crea para evitar tener que introducirlo como parametro de la clase
