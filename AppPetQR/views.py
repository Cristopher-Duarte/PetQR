from django.shortcuts import render

"""
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
"""

def Inicio(request):
    return render(request,"AppPetQR/Base.html")






