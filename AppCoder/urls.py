from django.urls import path

from AppCoder import views

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    # path('agrega-curso/<nombre>/<camada>', curso),
    # path('', inicio),
    # path('cursos', cursos),
    # path('profesores', profesores),
    # path('estudiantes', estudiantes),
    # path('entregables', entregables),
]
