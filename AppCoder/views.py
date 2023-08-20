from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.
def curso(req, nombre, camada):

    curso = Curso(nombre = nombre, camada = camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado</p>                       

    """)

def lista_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_culistarsos.html", {"lista_cursos": lista})