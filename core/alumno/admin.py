from django.contrib import admin
from .models import Especialidad,Alumno
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    list_display =("nombre","apellidoP","apellidoM","especialidad","fecha_creacion")
    list_filter = ["especialidad"]
    search_fields =("nombre","apellidoP","apellidoM")

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Especialidad)