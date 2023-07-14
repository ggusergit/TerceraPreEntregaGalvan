from django import forms

class VetFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    matricula = forms.IntegerField()
    especialidad = forms.CharField()

class DuenosFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    telefono = forms.IntegerField()
    direccion = forms.CharField()

class MascotaFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    tipo = forms.CharField()
    sexo = forms.CharField()

class TurnoFormulario(forms.Form):
    fecha = forms.DateField()
    hora = forms.IntegerField()

