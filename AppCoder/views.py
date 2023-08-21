from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

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

def inicio(req):

    return render(req, 'inicio.html')

def cursos(request):

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso = Curso( nombre = informacion['curso'], camada = informacion['camada'])

            curso.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = CursoFormulario()
    lista = Curso.objects.all()
    return render(request, "cursos.html", {"miFormulario": miFormulario, "lista_cursos": lista})

def profesores(req):

    return render(req, 'profesores.html')

def estudiantes(req):

    return render(req, 'estudiantes.html')

def entregables(req):

    return render(req, 'entregables.html')

def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso = Curso( nombre = informacion['curso'], camada = informacion['camada'])

            curso.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = CursoFormulario()

    return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})
    #     curso = Curso(nombre = request.POST['nombre'],camada = request.POST['camada'])

    #     curso.save()
    #     return render(request, "inicio.html")

    # return render(request, "cursoFormulario.html")

def profesorFormulario(request):

    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor = Profesor( nombre = informacion['nombre'], apellido = informacion['apellido'],
                                email = informacion['email'], profesion = informacion['profesion'])
            
            profesor.save()

            return render(request, "inicio.html")
        
    else:

        miFormulario = ProfesorFormulario()

    return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})