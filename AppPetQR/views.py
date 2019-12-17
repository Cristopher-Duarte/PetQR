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

from django.http.response import HttpResponseRedirect


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

"""
from django.views.generic.edit import FormView

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


def login_view(request, Username, Password):
    if request.method=='GET':
        return render(request, 'AppPetQR/IndexUsuario.html')
    else:
        
        user = authenticate(username=Username, password=Password)


       
        if user.is_usuario:
            login(request, user)
            
            return redirect(reverse('IndexUsuarios'))
        return render(request, 'AppPetQR/IndexUsuario.html')




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
                return redirect(reverse('login'))
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
            permiso = Permission.objects.get(name="Is Medico")

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


class PaginaRegistroMascota(View):
    def get(self, request, pk):
        Especies = Especie.objects.all()
        Razas = Raza.objects.all()

        Especies1 = Especie.objects.get(especie="Canino")
        Especies2 = Especie.objects.get(especie="Felino")

        GeneroMascotas = GeneroMascota.objects.all()
        Usuario = pk

        return render(request,'AppPetQR/Register/RegistroMascota.html',{'Especies':Especies, 
                                                                        'Razas':Razas, 
                                                                        'GeneroMascotas':GeneroMascotas,
                                                                        'Usuario':Usuario})

                                
def RegistrarMascota(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        Data_json = json.loads(data)

        especie =Especie.objects.get(id=int(Data_json["Especie"]))
        raza =Raza.objects.get(id=int(Data_json["Raza"]))
        usuario = Usuario.objects.get(id=int(Data_json["Usuario"]))
        generomascota =GeneroMascota.objects.get(id=int(Data_json["GeneroMascota"]))

        FormularioMascota = Mascotas(nombre = Data_json["Nombre"], fechanacimiento= Data_json["FechaNacimiento"],
                                     fk_especie=especie, fk_raza=raza, fk_usuario=usuario, 
                                     fk_generomascota=generomascota, foto=Data_json["Foto"])

        FormularioMascota.save()


    return redirect('LMostrarMascotas')


class PaginaRegistroVacunas(View):
    def get(self, request, pk):
        TipoProductos = TipoProducto.objects.get(nombre="Vacunas")
        Productos = Producto.objects.filter(fk_Tipoproducto= TipoProductos)
        Mascota = pk

        Efecto = Efectos.objects.all()

        return render(request, 'AppPetQR/Register/RegistroVacunas.html',{'Productos':Productos,
                                                                         'Efecto':Efecto,
                                                                         'Mascota':Mascota
                                                                            })
        

def RegistrarVacunas(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        Data_json = json.loads(data)
        Mascota = Mascotas.objects.get(id=int(Data_json["Mascota"]))
        Productos = Producto.objects.get(id=int(Data_json["Producto"]))

        FormularioVacuna = InfoVacunas(proximavacuna=Data_json["proximavacuna"], fk_mascota=Mascota,
                                    fk_producto = Productos)

        FormularioVacuna.save()  

        VacunaPk = len(InfoVacunas.objects.all())
        Vacuna =InfoVacunas.objects.get(id=VacunaPk)

        for date in Data_json["Efecto"]:
            efectos = Efectos.objects.get(id=date)
            FormularionDetalleVacuna = DetalleInfoVacunas(fk_efecto=efectos, fk_infovacuna=Vacuna)
            FormularionDetalleVacuna.save()



    return HttpResponse("Todo Bien Parce")


class PaginaRegistroControlesMedicos(View):
    def get(self, request, pk):
        TipoProductos = TipoProducto.objects.get(nombre="Medicamentos")
        Productos = Producto.objects.filter(fk_Tipoproducto= TipoProductos)

        Mascota = pk

        return render(request, 'AppPetQR/Register/RegistroControlMedico.html',{'Productos':Productos,
                                                                                'Mascota':Mascota})


class PaginaRegistroDesparasitacion(View):
    def get(self, request, pk):
        TipoProductos = TipoProducto.objects.get(nombre="Desparasitante")
        Productos = Producto.objects.filter(fk_Tipoproducto= TipoProductos)
        Mascota = pk

        return render(request, 'AppPetQR/Register/RegistroDesparacitacion.html',{'Productos':Productos,
                                                                                 'Mascota':Mascota})

def  RegistrarDesparasitacion(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        Data_json = json.loads(data)
        Productos =Producto.objects.get(id=Data_json[0])
        Mascota = Mascotas.objects.get(id=Data_json[2])
        FormularioDesparasitacion = InfoDesparacitacion(proximadesparacitante=Data_json[1], fk_producto=Productos, fk_mascota=Mascota)
        FormularioDesparasitacion.save()
        
    return HttpResponse("Todo Bien Parce")
    

#---------------Listar Movil---------------#

class ListarVacunasMovil(View):
    def get(self, request, pk):
        User = request.user.username
        dueño = Usuario.objects.get(documento=User)
        VacunasDate= InfoVacunas.objects.filter(fk_mascota=pk)
        MostMas= Mascotas.objects.get(id=pk)
        return render(request,'AppPetQR/Movil/List/ListarVacunas.html', {'VacunasDate':VacunasDate, 'dueño':dueño,'MostMas':MostMas})

class MostrarDesparasitanteMovil(View):
    def get(self, request):
        User = request.user.username
        pk = Usuario.objects.get(documento=User)
        dueño = Usuario.objects.get(documento=User)
        MascotaDate = Mascotas.objects.filter(fk_usuario=pk)
        return render(request,'AppPetQR/Movil/List/Desparasitante.html', {'MascotaDate':MascotaDate,'dueño':dueño})


class ListarControlMedicoMedicoMovil(View):
    def get(self, request):
        pass

class MostrarVacunaMovil(View):
    def get(self, request):
        User = request.user.username
        pk = Usuario.objects.get(documento=User)
        dueño = Usuario.objects.get(documento=User)
        MascotaDate = Mascotas.objects.filter(fk_usuario=pk)
        return render(request,'AppPetQR/Movil/List/Vacuna.html', {'MascotaDate':MascotaDate,'dueño':dueño})








#-----------Menu--------------------#
class ListarDesparacitacionMovil(View):
    def get(self, request):
        User = request.user.username
        pk = Usuario.objects.get(documento=User)
        dueño = Usuario.objects.get(documento=User)
        MascotaDate = Mascotas.objects.filter(fk_usuario=pk)
        return render(request,'AppPetQR/Movil/List/Desparasitante.html', {'MascotaDate':MascotaDate,'dueño':dueño})

class ListarMacotasMovil(View):
    def get(self, request):
        User = request.user.username
        pk = Usuario.objects.get(documento=User)
        dueño = Usuario.objects.get(documento=User)
        MascotaDate = Mascotas.objects.filter(fk_usuario=pk)
        return render(request,'AppPetQR/Movil/List/ListarMascota.html', {'MascotaDate':MascotaDate,'dueño':dueño})

#-----------Listar Administrador--------------------#

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

#-----------Listar Medico--------------------#
class MostrarUsuarioMedico(View):
    def get(self, request):
        user= request.user.username

        pk_Medico = MedicoVeterinaria.objects.get(documento=user)
        pk_Veterinaria = pk_Medico.fk_veterinaria
        usuarios  = Usuario.objects.all()
        return render(request, 'AppPetQR/List/MostrarUsuarioM.html',{'usuarios':usuarios,
                                                                     'pk_Veterinaria':pk_Veterinaria})

class MostrarMascotasMedico(View):
    def get(self, request, pk):
        MascotaDate = Mascotas.objects.filter(fk_usuario=pk)
        
        return render(request, 'AppPetQR/List/MostrarMascotasM.html', {'MascotaDate':MascotaDate})

class MostrarMascotasMedico(View):
    def get(self, request, pk):
        MascotaDate = Mascotas.objects.filter(fk_usuario=pk)
        
        return render(request, 'AppPetQR/List/MostrarMascotasM.html', {'MascotaDate':MascotaDate})

class MostrarVacunasMedico(View):
    def get(self, request, pk):
        VacunasDate= InfoVacunas.objects.filter(fk_mascota=pk)
 
        
        
        return render(request, 'AppPetQR/List/MostrarVacunasM.html', {'VacunasDate':VacunasDate})

class MostrarDesparasitacionMedico(View):
    def get(self, request , pk):
        Desparasitacion= InfoDesparacitacion.objects.filter(fk_mascota=pk)
 
        return render(request, 'AppPetQR/List/MostrarDesparasitacionM.html', {'Desparasitacion':Desparasitacion})


@login_required
def home (request):
    user = request.user
    if user.has_perm('AppPetQR.is_usuario'):
        return redirect(reverse('IndexUsuarios'))
    elif user.has_perm('AppPetQR.is_admin'):
        return redirect(reverse('IndexAdmin'))
    elif user.has_perm('AppPetQR.is_medico'):
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

