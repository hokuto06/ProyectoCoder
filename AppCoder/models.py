from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(null=True, max_length=30)
    email = models.EmailField(null=True)

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(null=True, max_length=30)
    email = models.EmailField(null=True)
    profesion = models.CharField(null=True, max_length=30)

class Profesor(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(null=True, max_length=30)
    email = models.EmailField(null=True)
    profesion = models.CharField(null=True, max_length=30)
    
class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()


