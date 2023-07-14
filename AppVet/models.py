from django.db import models

# Create your models here.

class Veterinario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    matricula = models.IntegerField()
    especialidad = models.CharField(max_length=15)

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=12)
    sexo = models.CharField(max_length=10)

class Dueño(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=30)

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.IntegerField()