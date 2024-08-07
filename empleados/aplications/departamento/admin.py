from atexit import register
from django.contrib import admin
from .models import Departamento
# Register your models here.

class DepartamentoAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'sigla',
        'activo',
        'piso',
        'oficina',
    )
admin.site.register(Departamento,DepartamentoAdmin)