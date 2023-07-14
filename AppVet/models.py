from django.db import models

# Create your models here.

class Veterinario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    matricula = models.IntegerField()
    especialidad = models.CharField(max_length=15)

    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} Matricula: {self.matricula} Especialidad: {self.especialidad}'

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=12)
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return f'Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo} Sexo: {self.sexo}'

class Dueño(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad} Telefono: {self.telefono} Direccion: {self.direccion}'

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.IntegerField()

    def __str__(self):
        return f'Fecha: {self.fecha} Hora: {self.hora}'