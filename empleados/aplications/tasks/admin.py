from django.contrib import admin
from .models import Menu,Categoria,Productos

# Register your models here.
class MenuAdmin (admin.ModelAdmin):




    list_display = (
        'nombre',
        'precio',
        'imagen',
        
       
    )

class CategoriaAdmin (admin.ModelAdmin):

    list_display =(
        'nombre',
        
      
        
    )

class ProductosAdmin (admin.ModelAdmin):
    lis_display =(
        'nombre',
        'precio',
        'imagen',
        'categoria',
        'codigo',
        'imagen',

        
    )



admin.site.register(Menu,MenuAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Productos,ProductosAdmin)
