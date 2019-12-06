from AppPetQR.views import *
from django.urls import *
from AppPetQR import views
from .models import *





urlpatterns = [
    path('Inicio',Inicio,name="inicio"),
    path('/Vacunas',Vacunas,name="vacuna"),
    path('/Control',Control,name="control"),
    path('/Desparacitacion',Desparacitacion,name="desparacitacion"),
    path('/Almacen',Almacen,name="almacen"),
    path('/Recordatorio',Recordatorio,name="recordatorio"),

    path('Veterinaria/Lista',Veterinaria_List, name="VeterinariaList"),
    path('Veterinaria/Agregar',Veterinaria_view,name="VeterinariaCrear"),
    path('Veterinaria/Editar/<int:id>',Veterinaria_edit,name="VeterinariaEditar"),
    path('Veterinaria/Borrar/<int:id>',Veterinaria_delete,name="VeterinariaBorrar"),
    
    #path('/login',login.as_view(),name="login"),

    #path('Veterinarias',LoginView.as_view(),name="Veterinarias"),




]