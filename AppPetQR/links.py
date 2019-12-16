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
    
    path('RegistroMedico/<int:pk>',login_required(RegistroMedico.as_view()),name="RMedico"),
    path('RegistroProducto/<int:pk>',login_required(RegistroProducto.as_view()),name="RProducto"),
    


    path('PaginaRegistroMascota/<int:pk>',login_required(PaginaRegistroMascota.as_view()),name="PaginaRegistroMascota"),
    path('PaginaRegistroMascota/RegistrarMascota/',login_required(RegistrarMascota)),

    #Registro Vacunas
    path('PaginaRegistroVacunas/<int:pk>',login_required(PaginaRegistroVacunas.as_view()),name="PaginaRegistroVacunas"),
    path('PaginaRegistroVacunas/RegistrarVacunas/',login_required(RegistrarVacunas)),

    
    #Fin registro Vacunas
    path('PaginaRegistroControlesMedicos/<int:pk>',login_required(PaginaRegistroControlesMedicos.as_view()),name="PaginaRegistroControlesMedicos"),
    path('PaginaRegistroControlesMedicos/RegistrarVacunas/',login_required(RegistrarVacunas)),
    #Registro Control Medico
    
    
    
    #Fin Registro Control Medico

    #Registro Desparasitantes

    #Fin Registro Desparasitantes


    #------------------------Listas------------------------------------------------------------------#
    path('ListarVacunas/',login_required(ListarVacunasMovil.as_view()),name="LVacunas"),
    path('ListarDesparacitacion/',login_required(ListarDesparacitacionMovil.as_view()),name="LDesparacitacion"),


    path('MostrarUsuario/',login_required(MostrarUsuario.as_view()),name="LMostrarUsuario"),
    path('MostrarVacunas/',login_required(MostrarVacunas.as_view()),name="LMostrarVacunas"),
    path('MostrarMascotas/',login_required(MostrarMascotas.as_view()),name="LMostrarMascotas"),
    path('MostrarControlesMedicos/',login_required(MostrarControlesMedicos.as_view()),name="LMostrarControlesMedicos"),
    path('MostrarDesparasitacion/',login_required(MostrarDesparasitacion.as_view()),name="LMostrarDesparasitacion"),
    path('MostrarProducto/',login_required(MostrarProducto.as_view()),name="LMostrarProducto"),



    path('', LoginView.as_view(template_name="Accounts/Login.html"), name='login'),


    path('LogoutSesion/',login_required(LogoutView.as_view(template_name='accounts/logout.html')),name='logout'),
    path('User/Index/',login_required(Index_Usuario),name='IndexUsuarios'),
    path('Home/Users',login_required(home),name='Home'),
    path('Admin/Index/',login_required(Index_Admin),name='IndexAdmin'),
    path('Doc/Index/',login_required(Index_Doctor),name='IndexDoctor'),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
