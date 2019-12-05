from AppPetQR.views import *
from django.urls import *
from AppPetQR import views
from .models import *





urlpatterns = [
    path('Inicio',Inicio,name="inicio"),
    #path('/login',login.as_view(),name="login"),

    #path('Veterinarias',LoginView.as_view(),name="Veterinarias"),

    path('RegistroVeterinaria',RegistroVeterinaria.as_view(),name='RegistroVeterinaria'),
    path('Veterinarias/Listado',ListarVeterinaria.as_view(),name='ListaVete'),


]