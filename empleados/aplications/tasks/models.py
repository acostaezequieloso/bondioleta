from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Menu (models.Model):



    nombre = models.CharField('Nombre', max_length=60)
   
    descripcion = models.TextField(default="Descripción predeterminada")
    precio = models.DecimalField(  max_digits=5, decimal_places=2, default=0.0)
    
    imagen=models.CharField(max_length=250, default='default_image.png')
    



    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
    


    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=250)
    slug=AutoSlugField(populate_from='nombre')
    activo=models.BooleanField(default=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='categoria'


class Productos(models.Model):
    codigo=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=250)
    slug=AutoSlugField(populate_from='nombre')
    imagen=models.CharField(max_length=250)
    descripcion=models.TextField(blank=True,null=True)
    precio=models.DecimalField(max_digits=15,decimal_places=2,default=0.0)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    destacado=models.BooleanField(default=True)
    activo=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='Producto'

