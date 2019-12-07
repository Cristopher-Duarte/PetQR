from django.shortcuts import render, redirect
from django.views.generic import View
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
    return render(request,"AppPetQR/Listas/vacunas.html")

def Control(request):
    return render(request,"AppPetQR/Listas/controlmedico.html")

def Desparacitacion(request):
    return render(request,"AppPetQR/Listas/desparacitacion.html")

def Almacen(request):
    return render(request,"AppPetQR/Listas/almacen.html")

def Recordatorio(request):
    return render(request,"AppPetQR/Listas/recordatorio.html")


#---------------Registros---------------#

class RegistroVeterinaria(View):
    def get(self, request):
        Formulario = VeterinariaForm

        return render(request, 'AppPetQR/Register/RegistroVeterinaria.html',{'form':Formulario})


    def post(self, request):
        if request.method == 'POST':
            Formulario = VeterinariaForm(request.POST)
            if Formulario.is_valid():
                Formulario.save()
        else:
            Formulario = VeterinariaForm()

        return render(request, 'AppPetQR/Register/RegistroVeterinaria.html', {'form':Formulario})       



class RegistroUsuario(View):
    def get(self,request, pk):
        FormularioU = UsuarioForm
        return render(request, 'AppPetQR/Register/RegistroUsuario.html',{'form':FormularioU})




    def post(self,request, pk):
        if request.method == 'POST':
            
            VeterinariaDate = Veterinaria.objects.get(id=pk) #objecto de la veterinaria

            FormularioU = UsuarioForm(request.POST)

            forms = FormularioU.save(commit=False)

            forms.fk_veterinaria = VeterinariaDate

            if FormularioU.is_valid():
                forms.save()
                return render(request, 'AppPetQR/Register/RegistroMedico.html',{'form':FormularioU})


class RegistroMedico(View):
    def get(self,request, pk):
        FormularioU = MedioForm
        return render(request, 'AppPetQR/Register/RegistroMedico.html',{'form':FormularioU})




    def post(self,request, pk):
        if request.method == 'POST':
            
            VeterinariaDate = Veterinaria.objects.get(id=pk) #objecto de la veterinaria

            FormularioU = MedioForm(request.POST)

            forms = FormularioU.save(commit=False)

            forms.fk_veterinaria = VeterinariaDate

            if FormularioU.is_valid():
                forms.save()
                return render(request, 'AppPetQR/Register/RegistroMedico.html',{'form':FormularioU})


class RegistroMascotas(View):
    def get(self, request, pk):
        FormularioM = MascotaForm
        return render(request, 'AppPetQR/Register/RegistroMascota.html',{'form':FormularioM})



    def post(self, request, pk):
        UsuarioDate= Usuario.objects.get(id=pk)

        FormularioM = MascotaForm(request.POST)


        forms = FormularioM.save(commit=False)

        forms.fk_usuario = UsuarioDate

        if FormularioM.is_valid():
            forms.save()
            return render(request, 'AppPetQR/Register/RegistroUsuario.html',{'form':FormularioM})


class RegistroProducto(View):

    def get(self, request, pk):
        FormularioP = ProductoForm
        return render(request, 'AppPetQR/Register/RegistroProducto.html',{'form':FormularioP})



    def post(self, request, pk):
        VeterinariaDate = Veterinaria.objects.get(id=pk) #objecto de la veterinaria

        FormularioP = ProductoForm(request.POST)


        forms = FormularioP.save(commit=False)

        forms.fk_veterinaria = VeterinariaDate

        if FormularioP.is_valid():
            forms.save()
            return render(request, 'AppPetQR/Register/RegistroProducto.html',{'form':FormularioP})
        

class RegistroVacunas(View):
    def get():
        pass

    def post():
        pass









