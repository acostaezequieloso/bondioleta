from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField



class Habilidades (models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de empleado'
        ordering = ['habilidad']
        unique_together = ('habilidad',)

    def __str__(self):
        return self.habilidad


class Empleado (models.Model):

    JOB_CHOICES =(
    ('0','Contador'),
    ('1','Administrativo'),
    ('2','Desarrollador'),
    ('3','Analista Funcional'),
    ('4','Otro'),)


    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=60)
    fecha_nac = models.DateField('Fecha de nacimiento', default= '1960-1-1', auto_now=False, auto_now_add=False)
    trabajo = models.CharField('Puesto', max_length=1, choices= JOB_CHOICES)

    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    imagen = models.ImageField(upload_to = "imagen" , null=True)
    observaciones = RichTextField(blank=True, null=True)


    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-nombre', 'apellido']
        unique_together = ('nombre', 'departamento',)

        def __str__(self):
            return self.nombre + ' - ' + self.apellido