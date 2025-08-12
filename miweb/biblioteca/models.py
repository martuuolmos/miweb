from django.db import models
#from .models import Libro

# Create your models here.
class Libro (models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
        

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre