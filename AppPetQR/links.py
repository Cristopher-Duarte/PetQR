from AppPetQR.views import *
from django.urls import *

from .models import *
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    #Esto no se referencia en ningun lado esto es movil <-------MOVIL-------->
    path('',Inicio,name="inicio"),
    path('Vacunas/',Vacunas,name="vacuna"),
    path('Control/',Control,name="control"),
    path('Desparacitacion/',Desparacitacion,name="desparacitacion"),
    path('Almacen/',Almacen,name="almacen"),
    path('Recordatorio/',Recordatorio,name="recordatorio"),
    #<--------FIN MOVIL--------->


    path('RegisterVeterinaria/',RegistroVeterinaria.as_view(),name="Rveterinaria"),
    path('RegisterUsuario/<int:pk>',RegistroUsuario.as_view(),name="RUsuario"),
    path('RegisterMascota/<int:pk>',RegistroMascotas.as_view(),name="RMascota"),
    path('RegistroMedico/<int:pk>',RegistroMedico.as_view(),name="RMedico"),
    path('RegistroProducto/<int:pk>',RegistroProducto.as_view(),name="RProducto"),
    path('RegistroDesparacitacion/<int:pk>',RegistroDesparacitacion.as_view(),name="RDesparacitacion"),
    





]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)