from django.db import models
from applications.departamento.models import Departamento
#from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model): #El par empleados-habilidades es ManyToMany - (Usamos m2mField)
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
    
    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    """Modelo para empleado"""
    JOB_CHOICES = {
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    }
    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    """Valores concretos entre unos pocos dados (choices)"""
    full_name = models.CharField('Nombres Completos', max_length=120, blank=True)

    job = models.CharField('Trabajo',max_length=50, choices=JOB_CHOICES)
    """El campo departamento es un foreign key"""
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    """Esta es una relacion particular, las hay de 1-1 de 1-muchos o de muchos-1"""
    #image = models.ImageField() sql3 no pilla muy bien las imagenes.
    habilidades = models.ManyToManyField(Habilidades)
    #hoja_vida = RichTextField(); # Permite añadir un campo de texto. 
    avatar = models.ImageField(upload_to='empleado', blank = True, null=True)
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleado de la empresa'
        ordering = ['first_name', 'last_name']
        unique_together = ['first_name', 'departamento']

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name