from django.shortcuts import render
from AppVet.models import *
from AppVet.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'AppVet/inicio.html')

def padre(request):
    return render(request, 'AppVet/padre.html')

def veterinario(request):
    return render(request, 'AppVet/veterinario.html')

def mascota(request):
    return render(request, 'AppVet/mascota.html')

def dueno(request):
    return render(request, 'AppVet/dueno.html')

def turno(request):
    return render(request, 'AppVet/turno.html')

def buscarVet(request):
    if request.GET['apellido']:

        apellido = request.GET['apellido']
        veterinario = Veterinario.objects.filter(apellido__icontains=apellido)
        contexto = {'veterinario':veterinario}

        return render(request, 'AppVet/veterinario.html', contexto)
    else:
        respuesta = 'No enviaste datos'

    return render(request, 'AppVet/veterinario.html', {'respuesta':respuesta})

def buscarMasc(request):
    if request.GET['nombre']:

        nombre = request.GET['nombre']
        mascota = Mascota.objects.filter(nombre__icontains=nombre)
        contexto = {'mascota':mascota}

        return render(request, 'AppVet/mascota.html', contexto)
    
    else:
        respuesta = 'No enviaste datos'
    
    return render(request, 'AppVet/mascota.html', {'respuesta':respuesta})

def buscarTurno(request):
    if request.GET['fecha']:

        fecha = request.GET['fecha']
        turno = Turno.objects.filter(fecha__icontains=fecha)
        contexto = {'turno':turno}

        return render(request, 'AppVet/turno.html', contexto)
    
    else:
        respuesta = 'No enviaste datos'
    
    return render(request, 'AppVet/mascota.html', {'respuesta':respuesta})

def buscarDue(request):
    if request.GET['apellido']:

        apellido = request.GET['apellido']
        dueno = Dueño.objects.filter(apellido__icontains=apellido)
        contexto = {'dueno':dueno}

        return render(request, 'AppVet/dueno.html', contexto)
    else:
            respuesta = 'No enviaste datos'
        
    return render(request, 'AppVet/mascota.html', {'respuesta':respuesta})      





