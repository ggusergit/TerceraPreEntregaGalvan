from django.contrib import admin
from django.urls import path
from AppVet.views import *

urlpatterns = [
    path('', inicio),
    path('inicio', inicio, name='Inicio'),
    path('veterinario', veterinario, name='Veterinario'),
    path('mascota', mascota, name='Mascota'),
    path('dueno', dueno, name='Dueno'),
    path('turno', turno, name='Turno'),
    path('buscarVet/', buscarVet),
    path('buscarMas/', buscarMasc),
    path('buscarTur/', buscarTurno),
    path('buscarDue/', buscarDue),
    path('vetFormulario', vetFormulario, name='VetFormulario'),
    path('masFormulario', masFormulario, name='MasFormulario'),
    path('dueFormulario', dueFormulario, name='DueFormulario'),
    path('turFormulario', turFormulario, name='TurFormulario'),
    
]