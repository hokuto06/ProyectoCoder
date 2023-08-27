from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
#Decorador por defecto
from django.contrib.auth.decorators import login_required

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

@login_required
def inicio(req):

    return render(req, 'inicio.html')

@login_required
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

@login_required
def profesores(req):

    listaProfesores = Profesor.objects.all()
    return render(req, 'profesores.html', {"lista_profesores": listaProfesores})

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

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})
            else:

                return render(request, "inicio.html", {"mensaje": f'Error, datos incorrectos'})        
        else:

            return render(request, "inicio.html", {"mensaje": f'Error, Formulario incorrecto'})
    
    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html")
        
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()

    return render(request,"registro.html", {"form":form})