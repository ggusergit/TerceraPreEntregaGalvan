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

def vetFormulario(request):
    if request.method == "POST":
        miFormulario = VetFormulario(request.POST) # donde llega la información del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            vet = Veterinario(nombre=informacion['nombre'], apellido=informacion['apellido'], matricula=informacion['matricula'], especialidad=informacion['especialidad'] )
            vet.save()
            
            return render(request, 'AppVet/inicio.html')
    else:
        miFormulario = VetFormulario()

    return render(request, 'AppVet/vetFormulario.html', {"miFormulario": miFormulario})

def masFormulario(request):
    if request.method == "POST":
        miFormulario = MascotaFormulario(request.POST) # donde llega la información del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            masc = Mascota(nombre=informacion['nombre'], edad=informacion['edad'], tipo=informacion['tipo'], sexo=informacion['sexo'] )
            masc.save()
            
            return render(request, 'AppVet/inicio.html')
    else:
        miFormulario = MascotaFormulario()

    return render(request, 'AppVet/masFormulario.html', {"miFormulario": miFormulario})

def dueFormulario(request):
    if request.method == "POST":
        miFormulario = DuenosFormulario(request.POST) # donde llega la información del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            due = Dueño(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], telefono=informacion['telefono'], direccion=informacion['direccion'])
            due.save()
            
            return render(request, 'AppVet/inicio.html')
    else:
        miFormulario = DuenosFormulario()

    return render(request, 'AppVet/dueFormulario.html', {"miFormulario": miFormulario})

def turFormulario(request):
    if request.method == "POST":
        miFormulario = TurnoFormulario(request.POST) # donde llega la información del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            tur = Turno(fecha=informacion['fecha'], hora=informacion['hora'])
            tur.save()
            
            return render(request, 'AppVet/inicio.html')
    else:
        miFormulario = TurnoFormulario()

    return render(request, 'AppVet/turFormulario.html', {"miFormulario": miFormulario})




