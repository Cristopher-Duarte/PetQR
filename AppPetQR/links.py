from AppPetQR.views import *
from django.urls import path
from AppPetQR import views
from .models import *
urlpatterns = [
    path('Inicio',Inicio,name="inicio")
    #path('/login',login.as_view(),name="login"),
]