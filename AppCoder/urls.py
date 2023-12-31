from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name = 'Register'),
    path('logout', LoginView.as_view(template_name='logout.html'), name='Logout'),
    # path('agrega-curso/<nombre>/<camada>', curso),
    # path('', inicio),
    # path('cursos', cursos),
    # path('profesores', profesores),
    # path('estudiantes', estudiantes),
    # path('entregables', entregables),
]
