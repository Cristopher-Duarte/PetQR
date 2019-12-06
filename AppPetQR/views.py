from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from AppPetQR.models import *
from AppPetQR.Forms import *

"""
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
"""

def Inicio(request):
    return render(request,"Movil.html")

def Vacunas(request):
    return render(request,"AppPetQR/vacunas.html")

def Control(request):
    return render(request,"AppPetQR/control-medico.html")

def Desparacitacion(request):
    return render(request,"AppPetQR/desparacitacion.html")

def Almacen(request):
    return render(request,"AppPetQR/almacen.html")

def Recordatorio(request):
    return render(request,"AppPetQR/recordatorio.html")


#----------VETERINARIA----------#

def Veterinaria_view(request):
    if request.method == 'POST':
        form = VeterinariaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('VeterinariaList')
    else:
        form = VeterinariaForm()

    return render(request, 'RegistroVeterinaria_Form.html', {'form':form})

def Veterinaria_List(request):
    veterinaria = Veterinaria.objects.all()
    contexto = {'veterinaria':veterinaria}
    return render(request, 'ListaVete.html', contexto)

def Veterinaria_edit(request, id):
    veterinaria = Veterinaria.objects.get(id=id)
    if request.method == 'GET':
        form = VeterinariaForm(instance=veterinaria)
    else:
        form = VeterinariaForm(request.POST, instance=veterinaria)
        if form.is_valid():
            form.save()
        return redirect('VeterinariaList')
    return render(request, 'RegistroVeterinaria_Form.html', {'form':form}) 

def Veterinaria_delete(request, id):
    veterinaria = Veterinaria.objects.get(id=id)
    if request.method == 'POST':
        veterinaria.delete()
        return redirect('VeterinariaList')
    return render(request, 'EliminarVeterinarias.html', {'veterinaria':veterinaria})


