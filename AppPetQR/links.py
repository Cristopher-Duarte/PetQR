from AppPetQR.views import *
from django.urls import *


from .models import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required






urlpatterns = [



    #Esto no se referencia en ningun lado esto es movil <-------MOVIL-------->
    path('Inicio/<int:pk>',MostrarMascotas.as_view(),name="inicio"),
    #path('Vacunas/',Vacunas,name="vacuna"),
    path('Control/',Control,name="control"),
    path('Desparacitacion/',Desparacitacion,name="desparacitacion"),
    path('Almacen/',Almacen,name="almacen"),
    path('Recordatorio/',Recordatorio,name="recordatorio"),
    #<--------FIN MOVIL--------->

    #------------------------Registros------------------------------------------------------------------#
    path('RegisterVeterinaria/',RegistroVeterinaria.as_view(),name="Rveterinaria"),
    path('RegisterUsuario/<int:pk>',login_required(RegistroUsuario.as_view()),name="RUsuario"),
    path('RegisterMascota/<int:pk>',login_required(RegistroMascotas.as_view()),name="RMascota"),
    path('RegistroMedico/<int:pk>',login_required(RegistroMedico.as_view()),name="RMedico"),
    path('RegistroProducto/<int:pk>',login_required(RegistroProducto.as_view()),name="RProducto"),
    path('RegistroDesparacitacion/<int:pk>',login_required(RegistroDesparacitacion.as_view()),name="RDesparacitacion"),

    #Registro Vacunas
    path('RegistroVacunas/<int:pk>',login_required(RegistroVacunas.as_view()),name="RVacunas"),
    path('RegistroDetalleVacuna/',login_required(RegistroDetalleVacuna.as_view()),name="RDatelleVacuna"),
    path('RegistroDetalleVacuna/Register/',login_required(RegisterVacuna)),
    #Fin registro

    #Registro Control Medico
    path('RegistroControlMedico/<int:mascota>',login_required(RegistroControlMedico.as_view()),name="RControlMedico"),
    path('RegistroDetalleControlMedico/<int:pk>',login_required(RegistroDetalleControlMedico.as_view()),name="RDetalleControlMedico"),
    path('RegistroDetalleControlMedico/Register',login_required(RegisterControlMedico)),
    #Fin Registro




    #------------------------Listas------------------------------------------------------------------#
    path('ListarVacunas/',login_required(ListarVacunasMovil.as_view()),name="LVacunas"),
    path('ListarDesparacitacion/',login_required(ListarDesparacitacionMovil.as_view()),name="LDesparacitacion"),


    path('MostrarUsuario/',login_required(MostrarUsuario.as_view()),name="LMostrarUsuario"),
    path('MostrarVacunas/',login_required(MostrarVacunas.as_view()),name="LMostrarVacunas"),
    path('MostrarMascotas/',login_required(MostrarMascotas.as_view()),name="LMostrarMascotas"),
    path('MostrarControlesMedicos/',login_required(MostrarControlesMedicos.as_view()),name="LMostrarControlesMedicos"),
    path('MostrarDesparasitacion/',login_required(MostrarDesparasitacion.as_view()),name="LMostrarDesparasitacion"),
    path('MostrarProducto/',login_required(MostrarProducto.as_view()),name="LMostrarProducto"),



    path('', LoginView.as_view(template_name="accounts/login.html"), name='login'),

    path('LogoutSesion/',login_required(LogoutView.as_view(template_name='accounts/logout.html')),name='logout'),
    path('User/Index/',login_required(Index_Usuario),name='IndexUsuarios'),
    path('Home/Users',login_required(home),name='Home'),
    path('Admin/Index/',login_required(Index_Admin),name='IndexAdmin'),
    path('Doc/Index/',login_required(Index_Doctor),name='IndexDoctor'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
