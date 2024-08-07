from atexit import register

from django.contrib import admin
from django.http import HttpResponse
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Empleado,Habilidades
from django.db import models 
from ckeditor.widgets import CKEditorWidget

from datetime import date


# Register your models here.

admin.site.register(Habilidades)

formfield_overrides={
    models.TextField:{'Widget':CKEditorWidget()},
}

class EmpleadoAdmin (admin.ModelAdmin):

    def calcularEdad(self,obj):
        today = date.today()
        age = today.year - obj.fecha_nac.year - ((today.month, today.day) < (obj.fecha_nac.month, obj.fecha_nac.day))
        return age

    calcularEdad.short_description = 'Edad'



    list_display = (
        'nombre',
        'apellido',
        'trabajo',
        'fecha_nac',
        'calcularEdad',
        'departamento',
        'observaciones',
        'id',
    )

    search_fields =(
        'apellido',
        'nombre',
        'id',
    )

    list_filter =(
        'departamento',
        'trabajo',
       

    )

    filter_horizontal = (
         'habilidades',
    )

    def export_selected_to_csv(modeladmin,request, queryset):

        # Lógica para exportar a CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="empleados.csv"'

        writer = csv.writer(response)
        writer.writerow(['Nombre', 'Apellido', 'Trabajo', 'Departamento'])

        for empleado in queryset:
            writer.writerow([empleado.nombre, empleado.apellido, empleado.trabajo, empleado.departamento , empleado.imagen])

        return response

        export_selected_to_csv.short_description = "Exportar empleados seleccionados a CSV"


    def export_selected_to_pdf(modeladmin,request, queryset):
                # Lógica para exportar a PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="empleados.pdf"'

        buffer = canvas.Canvas(response, pagesize=letter)

        buffer.drawString(100, 750, "Lista de Empleados:")

        y = 700

        for empleado in queryset:
            y -= 20
            buffer.drawString(100, y, f"Nombre: {empleado.nombre}")
            y -= 20
            buffer.drawString(100, y, f"Apellido: {empleado.apellido}")
            y -= 20
            buffer.drawString(100, y, f"Trabajo: {empleado.trabajo}")
            y -= 20
            buffer.drawString(100, y, f"Departamento: {empleado.departamento}")




        buffer.showPage()
        buffer.save()

        return response

        export_selected_to_pdf.short_description = "Exportar empleados seleccionados a PDF"

    actions = [export_selected_to_csv, export_selected_to_pdf]


    
    

      

admin.site.register(Empleado,EmpleadoAdmin)