from django import forms

#from apps.Veterinaria.models import *
from AppPetQR.models import *
class VeterinariaForm(forms.ModelForm):

    class Meta:
        model = Veterinaria

        fields = [
            'nombre',
            'logo',
            'correocoorporativo',
            'telefono',
        ]
        labels = {
            'nombre' : 'Nombre',
            'logo' : 'Logo',
            'correocoorporativo' : 'Correo Coorporativo',
            'telefono' : 'Telefono',            
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Veterinaria'}),
            'logo' : forms.TextInput(attrs={'class':'form-control'}),
            'correocoorporativo' : forms.TextInput(attrs={'class':'form-control','placeholder':'Correo Valido'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
        }
