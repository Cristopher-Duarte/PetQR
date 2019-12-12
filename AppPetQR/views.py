from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from AppPetQR.models import *
from AppPetQR.models import InfoVacunas, Usuario
from AppPetQR.Forms import *
from django.contrib import *
import json
from django.contrib.auth.decorators import login_required, permission_required
from django.http import *
from django.contrib.auth.models import Permission, User
from AppPetQR.VerificarUsuario import Verificador



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
    return render(request,"AppPetQR/List/ListarVacunas.html")

def Control(request):
    return render(request,"AppPetQR/List/controlmedico.html")

def Desparacitacion(request):
    return render(request,"AppPetQR/List/desparacitacion.html")

def Almacen(request):
    return render(request,"AppPetQR/List/almacen.html")

def Recordatorio(request):
    return render(request,"AppPetQR/List/recordatorio.html")



    



#---------------Registros---------------#

class RegistroVeterinaria(View):
    def get(self, request):
        Formulario = VeterinariaForm

        return render(request, 'AppPetQR/Register/RegistroVeterinaria.html',{'form':Formulario})


    def post(self, request):
        if request.method == 'POST':
            Formulario = VeterinariaForm(request.POST)
            username=request.POST.get("nombre")
            password = str(username)+"QR"
            permiso = Permission.objects.get(name="Is Admin")
            decision = Verificador("ADMIN", str(username))


            if Formulario.is_valid() and decision:
                Users=User.objects.create_user(username, "", password)
                Users.user_permissions.add(permiso)
                Users.save()
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
            
            username=request.POST.get("documento")
            password = str(username)+"QR"
            permiso = Permission.objects.get(name="Is Usuario")

            decision = Verificador("USER", str(username))

            forms.fk_veterinaria = VeterinariaDate

            if FormularioU.is_valid() and decision:
                Users=User.objects.create_user(username, "", password)
                Users.user_permissions.add(permiso)
                Users.save()
                forms.save()
                
                return redirect(reverse('LMostrarUsuario'))
            else:
                return render(request, 'AppPetQR/Register/RegistroUsuario.html',{'form':FormularioU})




class RegistroMedico(View):
    def get(self,request, pk):
        FormularioU = MedioForm
        return render(request, 'AppPetQR/Register/RegistroMedico.html',{'form':FormularioU})




    def post(self,request, pk):
        if request.method == 'POST':
            
            VeterinariaDate = Veterinaria.objects.get(id=pk) #objecto de la veterinaria

            FormularioU = MedioForm(request.POST)

            forms = FormularioU.save(commit=False)
                        
            username=request.POST.get("documento")
            password = str(username)+"QR"
            permiso = Permission.objects.get(name="Is Usuario")

            decision = Verificador("MEDICO", str(username))

            forms.fk_veterinaria = VeterinariaDate

            if FormularioU.is_valid() and decision:
                Users=User.objects.create_user(username, "", password)
                Users.user_permissions.add(permiso)
                Users.save()
                forms.save()
                return render(request, 'AppPetQR/Register/RegistroMedico.html',{'form':FormularioU})
            else:
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
            return redirect(reverse('LMostrarMascotas'))

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
            return redirect(reverse('LMostrarProducto'))

class RegistroDesparacitacion(View):

    def get(self, request, pk):
        id = TipoProducto.objects.filter(nombre="Medicamentos")
        FormularioD = InfoDesparacitacionForm(id)

        return render(request, 'AppPetQR/Register/RegistroDesparacitacion.html',{'form':FormularioD})      

    def post(self, request, pk):

       
        id = TipoProducto.objects.filter(nombre="Medicamentos")
        MascotasDate = Mascotas.objects.get(id=pk) #objecto de la veterinaria

        FormularioD = InfoDesparacitacionForm(id, request.POST)

        forms = FormularioD.save(commit=False)

        forms.fk_mascota = MascotasDate

        if FormularioD.is_valid():
            forms.save()
            return render(request, 'AppPetQR/Register/RegistroDesparacitacion.html',{'form':FormularioD})
   
class RegistroVacunas(View):

    def get(self, request, pk):
        id = TipoProducto.objects.filter(nombre="Medicamentos")
        FormularioV =InfoVacunasForm(id)

        return render(request, 'AppPetQR/Register/RegistroVacunas.html',{'form':FormularioV})


    def post(self, request, pk):
        id = TipoProducto.objects.filter(nombre="Medicamentos")
        MascotasDate = Mascotas.objects.get(id=pk) #objecto de la veterinaria
        FormularioV = InfoVacunasForm(id, request.POST)
        forms = FormularioV.save(commit=False)
        forms.fk_mascota = MascotasDate
        if FormularioV.is_valid():
            pk = len(InfoVacunas.objects.all())
            Date = InfoVacunas.objects.all()
            forms.numeroregistro = pk
            forms.save()

            
      
            return redirect(reverse('LMostrarVacunas'))

class RegistroDetalleVacuna(View):
    def get(self, request):
        VacunaDate= InfoVacunas.objects.all()
        EfectosDate = Efectos.objects.all()
        numero = len(InfoVacunas.objects.all())
        user= request.user.username
        pk = Veterinaria.objects.get(nombre=user)
        
        return render(request, 'AppPetQR/Register/RegistroDetalleVacuna.html', {'Date':VacunaDate, 'DatosEfectos':EfectosDate, 'user':pk, 'numero':numero})


class RegistroControlMedico(View):
    def get(self, request, mascota):
        FormularioCM=ControlesMedicosForm

        return render(request, 'AppPetQR/Register/RegistroControlMedico.html',{'form':FormularioCM})

    def post(self, request, mascota):    
        MascotasDate = Mascotas.objects.get(id=mascota)
        user= request.user.username

        MedicoDate= MedicoVeterinaria.objects.get(nombre=user)

        FormularioCM=ControlesMedicosForm(request.POST)
        forms= FormularioCM.save(commit=False)
        forms.fk_mascota = MascotasDate
        forms.fk_medicoveterinario = MedicoDate
        if FormularioCM.is_valid():
            forms.save()

            pk= len(ControlesMedicos.objects.all())
            return redirect(reverse('RDetalleControlMedico',kwargs={'pk': pk}))
        
class RegistroDetalleControlMedico(View):
    def get(self, request, pk):
        ControlMedicoDate= ControlesMedicos.objects.get(id=pk)
        TipoMedicamento = TipoProducto.objects.get(nombre="Medicamentos")
        MedicamentoDate = Producto.objects.filter(fk_Tipoproducto=TipoMedicamento)
        
        return render(request, 'AppPetQR/Register/RegistroControlMedico.html', {"MedicamentoDate":MedicamentoDate, "ControlMedicoDate":ControlMedicoDate})



def RegisterControlMedico(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        Data_json = json.loads(data)
        #print(c)
        data = Data_json[1:]
        #print(data)
        
        for x in data:
            pass




def RegisterVacuna(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        Data_json = json.loads(data)
        #print(c)
        data = Data_json[1:]
        #print(data)
        
        for x in data:
            efecto= Efectos.objects.get(id=x)
            #print(efecto)
            #print(c[0]["NumeroRegistro"])
            VacunaDate= InfoVacunas.objects.get(numeroregistro=(Data_json[0]["NumeroRegistro"]))
            #print(VacunaDate)
            forms=DetalleInfoVacunas(fk_efecto=efecto, fk_infovacuna=VacunaDate)
            forms.save()

       
            


    return HttpResponse("bien")

#---------------Listar Movil---------------#

class ListarVacunasMovil(View):
    def get(self, request):
        
        VacunaDate = DetalleInfoVacunas.objects.all()
        
             

        return render(request,'AppPetQR/Movil/List/ListarVacunas.html', {'VacunaDate':VacunaDate}) 
       
class ListarDesparacitacionMovil(View):
    def get(self, request, pk):
        DesparacitacionDate = InfoDesparacitacion.objects.filter(fk_mascota=pk)
        return render(request,'AppPetQR/Movil/List/ListarDesparacitacion.html', {'DesparacitacionDate':DesparacitacionDate})

class ListarControlMedicoMedicoMovil(View):
    def get(self, request):
        pass

class ListarMascota(View):
    def get(self, request):
        user= request.user.username   
        pk = Veterinaria.objects.get(nombre=user)
        MascotaDate = Mascotas.objects.all()
        return render(request, 'AppPetQR/IndexUsuario.html', {'form':MascotaDate, 'user':pk})
#-----------Listar --------------------#

class MostrarUsuario(View):
    def get(self, request):
        UsuarioDate= Usuario.objects.all()
        user= request.user.username
        pk = Veterinaria.objects.get(nombre=user)
        return render(request, 'AppPetQR/List/MostrarUsuario.html', {'form':UsuarioDate, 'user':pk})

class MostrarVacunas(View):
    def get(self, request):
        VacunasDate= InfoVacunas.objects.all()
        user= request.user.username
        pk = Veterinaria.objects.get(nombre=user)
        return render(request, 'AppPetQR/List/MostrarVacunas.html', {'form':VacunasDate, 'user':pk})

class MostrarControlesMedicos(View):
    def get(self, request):
        ControleMedicosDate= ControlesMedicos.objects.all()
        user= request.user.username
        pk = Veterinaria.objects.get(nombre=user)
        return render(request, 'AppPetQR/List/MostrarControlMedico.html', {'form':ControleMedicosDate})

class MostrarDesparasitacion(View):
    def get(self, request):
        user= request.user.username
        pk = Veterinaria.objects.get(nombre=user)
        InfoDesparacitacionDate=InfoDesparacitacion.objects.all()
        return render(request, 'AppPetQR/List/MostrarDesparasitacion.html', {'form':InfoDesparacitacionDate, 'user':pk})

class MostrarMascotas(View):
    def get(self, request):
        user= request.user.username   
        pk = Veterinaria.objects.get(nombre=user)
        MascotaDate = Mascotas.objects.all()
        return render(request, 'AppPetQR/List/MostrarMascotas.html', {'form':MascotaDate, 'user':pk})


class MostrarProducto(View):
    def get(self, request):
        user= request.user.username   
        pk = Veterinaria.objects.get(nombre=user)
        ProductoDate = Producto.objects.all()
        return render(request, 'AppPetQR/List/MostrarProducto.html', {'form':ProductoDate, 'user':pk})


@login_required
def home (request):
    user = request.user
    if user.has_perm('AppPetQR.is_usuario'):
        return redirect(reverse('IndexUsuarios'))
    elif user.has_perm('AppPetQR.is_admin'):
        return redirect(reverse('IndexAdmin'))
    elif user.has_perm('AppPetQR.is_doctor'):
        return redirect('IndexDoctor')
    

@permission_required('AppPetQR.is_usuario')
def Index_Usuario (request):
    return render (request, template_name='AppPetQR/IndexUsuario.html')

@permission_required('AppPetQR.is_admin')
def Index_Admin(request):
    return render (request, template_name='AppPetQR/indexAdmin.html')

@permission_required('AppPetQR.is_medico')
def Index_Doctor (request):
    return render(request, template_name='AppPetQR/indexDoctor.html')

