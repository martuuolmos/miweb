from django.shortcuts import render
from .models import Alumnos

# Crear las vistas del sitio.
def index(request):
    alumnos = Alumnos.objects.all()
    print(Alumnos) 
    return render (request, "index.html")

def pagina1(request):
    return render(request, "pagina1.html",{'Alumnos': Alumnos})

def pagina2(request):
    return render(request, "pagina2.html")