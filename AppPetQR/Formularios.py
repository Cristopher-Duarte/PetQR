from django import forms

from AppPetQR.models import *

class RegistroVeterinariaForm(forms.ModelForm):

    class Meta:
        model = Veterinaria

        fields =[
            'Nombre',
            'FechaResgistro',
            'Logo',
            'CorreoCoorporativo',
            'Estado',
            'Telefono',
        ]

        labels={
            'Nombre'         : 'Nombre',
            'FechaRegistro'  : 'FechaRegistro',
            'Logo'           : 'Logo',
            'CorreoCoorporativo' : 'CorreoCoorporativo',
            'Estado'          : 'Estado',
            'Telefono'       : 'Telefono',
        }

        widgets={       
            'Nombre'          : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Veterinaria'}), 
            'FechaRegistro'   : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/AAA'}), 
            'Logo'            : forms.TextInput(attrs={'class':'form-control'}), 
            'CorreoCoorporativo' : forms.TextInput(attrs={'class':'form-control','placeholder':'Correo Electronico Valido'}),
            'Estado'          : forms.TextInput(attrs={'class':'form-control'}),
            'Telefono'        : forms.TextInput(attrs={'class':'form-control'}),  
        }

# class ActualizarMedico(forms.ModelForm):
#     class Meta:
#         model = Medico

#         fields =[
#             'Documento',
#             'Nombres',
#             'PrimerApellido',
#             'SegundoApellido',
#             'Genero',
#             'Celular',
#             'Direccion'
#         ]

#         labels={
#             'Documento'       : 'Documento',
#             'Nombres'         : 'Nombres',
#             'PrimerApellido'  : 'PrimerApellido',
#             'SegundoApellido' : 'SegundoApellido',
#             'Genero'          : 'Genero',
#             'Celular'         : 'Celular',
#             'Direccion'       : 'Direccion',
#         }

#         widgets={
#             'Documento'       : forms.TextInput(attrs={'class':'form-control'}),        
#             'Nombres'         : forms.TextInput(attrs={'class':'form-control'}), 
#             'PrimerApellido'  : forms.TextInput(attrs={'class':'form-control'}), 
#             'SegundoApellido' : forms.TextInput(attrs={'class':'form-control'}), 
#             'Genero'          : forms.Select(attrs={'class':'form-control'}),
#             'Celular'         : forms.TextInput(attrs={'class':'form-control'}), 
#             'Direccion'       : forms.TextInput(attrs={'class':'form-control'}), 
#         }

# class RegistroClienteForm(forms.ModelForm):

#     class Meta:
#         model = Cliente

#         fields =[
#             'Documento',
#             'Nombres',
#             'PrimerApellido',
#             'SegundoApellido',
#             'FechaNacimiento',
#             'Genero',
#             'Celular',
#             'Direccion'
#         ]

#         labels={
#             'Documento'       : 'Documento',
#             'Nombres'         : 'Nombres',
#             'PrimerApellido'  : 'PrimerApellido',
#             'SegundoApellido' : 'SegundoApellido',
#             'FechaNacimiento' : 'FechaNacimiento',
#             'Genero'          : 'Genero',
#             'Celular'         : 'Celular',
#             'Direccion'       : 'Direccion',
#         }

#         widgets={
#             'Documento'       : forms.TextInput(attrs={'class':'form-control','placeholder':'Documento'}),        
#             'Nombres'         : forms.TextInput(attrs={'class':'form-control'}), 
#             'PrimerApellido'  : forms.TextInput(attrs={'class':'form-control'}), 
#             'SegundoApellido' : forms.TextInput(attrs={'class':'form-control'}), 
#             'FechaNacimiento' : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/AAA'}),
#             'Genero'          : forms.Select(attrs={'class':'form-control'}),
#             'Celular'         : forms.TextInput(attrs={'class':'form-control'}), 
#             'Direccion'       : forms.TextInput(attrs={'class':'form-control'}), 
#         }

# class ActualizarCliente(forms.ModelForm):
#     class Meta:
#         model = Cliente

#         fields =[
#             'Documento',
#             'Nombres',
#             'PrimerApellido',
#             'SegundoApellido',
#             'Genero',
#             'Celular',
#             'Direccion'
#         ]

#         labels={
#             'Documento'       : 'Documento',
#             'Nombres'         : 'Nombres',
#             'PrimerApellido'  : 'PrimerApellido',
#             'SegundoApellido' : 'SegundoApellido',
#             'Genero'          : 'Genero',
#             'Celular'         : 'Celular',
#             'Direccion'       : 'Direccion',
#         }

#         widgets={
#             'Documento'       : forms.TextInput(attrs={'class':'form-control'}),        
#             'Nombres'         : forms.TextInput(attrs={'class':'form-control'}), 
#             'PrimerApellido'  : forms.TextInput(attrs={'class':'form-control'}), 
#             'SegundoApellido' : forms.TextInput(attrs={'class':'form-control'}), 
#             'Genero'          : forms.Select(attrs={'class':'form-control'}),
#             'Celular'         : forms.TextInput(attrs={'class':'form-control'}), 
#             'Direccion'       : forms.TextInput(attrs={'class':'form-control'}), 
#         }

# class RegistroCitaForm(forms.ModelForm):
#     class Meta:
#         model = Citas

#         fields =[
#             'FechaCita',
#             'HoraCita',
#             'Medico',

#         ]

#         labels={
#             'FechaCita'  : 'FechaCita',
#             'HoraCita'   :  'HoraCita',
#             'Medico'     :    'Medico',

#         }

#         widgets={
#             'FechaCita' : forms.TextInput(attrs={'class':'form-control'}),        
#             'HoraCita'  : forms.TextInput(attrs={'class':'form-control'}), 
#             'Medico'    : forms.Select(attrs={'class':'form-control'}), 

           
#         }


# class RegistroMascotasForm(forms.ModelForm):
#     class Meta:

#         model=Mascotas
#         fields=[
#             'Nombre',
#             'FechaNacimiento',
#             'GeneroMascota',
#             'Raza',
#         ]

#         labels={
#             'Nombre'            :    'Nombre',
#             'FechaNacimiento'   :    'FechaNacimiento',
#             'GeneroMascota'     :    'Genero',
#             'Raza'              :    'Raza',
#         }
        
        
#         widgets={
#             'Nombre'            : forms.TextInput(attrs={'class':'form-control'}),        
#             'FechaNacimiento'   : forms.TextInput(attrs={'class':'form-control'}), 
#             'GeneroMascota'     : forms.Select(attrs={'class':'form-control'}), 
#             'Raza'              : forms.Select(attrs={'class':'form-control'}), 
           
#         }


# class RegistroDetalle(forms.ModelForm):
#     class Meta:

#         model=DetalleCita
#         fields=[
#             'Observacion',
#             'Medicamento',
#             'ExamenMascota',
#         ]

#         labels={
#             'Observacion'       :    'Observacion',
#             'Medicamento'       :    'Medicamento',
#             'ExamenMascota'     :    'Examenes'    ,
   
#         }
        
        
#         widgets={
#             'Observacion'       : forms.TextInput(attrs={'class':'form-control'}),        
#             'Medicamento'       : forms.Select(attrs={'class':'form-control', 'required': False}), 
#             'ExamenMascota'     : forms.Select(attrs={'class':'form-control', 'required': False}), 
           
#         }



