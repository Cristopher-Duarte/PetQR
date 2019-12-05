from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from AppPetQR.models import *

"""
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
"""

def Inicio(request):
    return render(request,"AppPetQR/Movil.html")

class RegistroVeterinaria(CreateView):
    model = Veterinaria
    template_name = 'RegistroVeterinaria.html' 
    form_class = CreateView
    success_url = reverse_lazy('ListaVeterinarias')

class ListarVeterinaria(ListView):
    model = Veterinaria
    template_name = 'ListaVete.html'
    form_class = ListView
    success_url = reverse_lazy('ListaVeterinaria')


