from django.db import models

# Create your models here.

class Especialidad (models.Model):
    nombre = models.CharField( verbose_name="Nombre de la Especialidad" ,max_length=100)

    class Meta:
        verbose_name_plural = "Especialidades"
        
    def __str__(self):
        return self.nombre

class Alumno (models.Model):
    numControl = models.CharField(verbose_name="Numero de control", max_length=50, unique=True)
    nombre = models.CharField(verbose_name="Nombre del alumno" , max_length=100)
    apellidoP = models.CharField(verbose_name="Apellido Paterno" , max_length=100)
    apellidoM = models.CharField(verbose_name="Apellido Materno" , max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =["nombre"]

    
    def __str__(self):
        return self.nombre

