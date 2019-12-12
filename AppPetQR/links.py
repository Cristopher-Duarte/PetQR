from AppPetQR.views import *
from django.urls import *

from .models import *
from django.conf import settings
from django.conf.urls.static import static





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
    path('RegisterUsuario/<int:pk>',RegistroUsuario.as_view(),name="RUsuario"),
    path('RegisterMascota/<int:pk>',RegistroMascotas.as_view(),name="RMascota"),
    path('RegistroMedico/<int:pk>',RegistroMedico.as_view(),name="RMedico"),
    path('RegistroProducto/<int:pk>',RegistroProducto.as_view(),name="RProducto"),
    path('RegistroDesparacitacion/<int:pk>',RegistroDesparacitacion.as_view(),name="RDesparacitacion"),

    #Registro Vacunas
    path('RegistroVacunas/<int:pk>',RegistroVacunas.as_view(),name="RVacunas"),
    path('RegistroDetalleVacuna/<int:pk>',RegistroDetalleVacuna.as_view(),name="RDatelleVacuna"),
    path('RegistroDetalleVacuna/Register/',RegisterVacuna),
    #Fin registro

    #Registro Control Medico
    path('RegistroControlMedico/<int:medico>/<int:mascota>',RegistroControlMedico.as_view(),name="RControlMedico"),
    path('RegistroDetalleControlMedico/<int:pk>',RegistroDetalleControlMedico.as_view(),name="RDetalleControlMedico"),
    path('RegistroDetalleControlMedico/Register',RegisterControlMedico),
    #Fin Registro
   
    
    

    #------------------------Listas------------------------------------------------------------------#
    path('ListarVacunas/<int:pk>',ListarVacunasMovil.as_view(),name="LVacunas"),
    path('ListarDesparacitacion/<int:pk>',ListarDesparacitacionMovil.as_view(),name="LDesparacitacion"),


    path('MostrarUsuario/',MostrarUsuario.as_view(),name="LMostrarUsuario"),
    path('MostrarVacunas/',MostrarVacunas.as_view(),name="LMostrarVacunas"),
    path('MostrarControlesMedicos/',MostrarControlesMedicos.as_view(),name="LMostrarControlesMedicos"),
    path('MostrarDesparasitacion/',MostrarDesparasitacion.as_view(),name="LMostrarDesparasitacion"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
