from django.contrib import admin
from django.urls import path,include
from AppPetQR.links import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('AppPetQR.links'))
]
