from django import forms
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


class UsuarioForm(forms.ModelForm):
    class Meta:

        model = Usuario

        fields=[
            'documento',
            'nombre',
            'apellido',
            'fechanacimiento',
            'correoelectronico',
            'celular',
            'fk_genero',
        ]

        labels={
            'documento'             :   'documento',
            'nombre'                :   'nombre',
            'apellido'              :   'apellido',
            'fechanacimiento'       :   'fechanacimiento',
            'correoelectronico'     :   'correoelectronico',
            'celular'               :   'celular',
            'fk_genero'             :   'genero',
        
        }
        widgets={
            'documento'             :   forms.TextInput(attrs={'class':'form-control'}),
            'nombre'                :   forms.TextInput(attrs={'class':'form-control'}),   
            'apellido'              :   forms.TextInput(attrs={'class':'form-control'}),
            'fechanacimiento'       :   forms.TextInput(attrs={'class':'form-control'}),
            'correoelectronico'     :   forms.TextInput(attrs={'class':'form-control'}),
            'celular'               :   forms.TextInput(attrs={'class':'form-control'}),
            'fk_genero'             :   forms.Select(attrs={'class':'form-control'}),         
        }

class MedioForm(forms.ModelForm):
    class Meta:

        model = MedicoVeterinaria

        fields=[
            'documento',
            'nombre',
            'apellido',
            'fechanacimiento',
            'correoelectronico',
            'celular',
            'fk_genero',
        ]

        labels={
            'documento'             :   'documento',
            'nombre'                :   'nombre',
            'apellido'              :   'apellido',
            'fechanacimiento'       :   'fechanacimiento',
            'correoelectronico'     :   'correoelectronico',
            'celular'               :   'celular',
            'fk_genero'             :   'genero',
        
        }
        widgets={
            'documento'             :   forms.TextInput(attrs={'class':'form-control'}),
            'nombre'                :   forms.TextInput(attrs={'class':'form-control'}),   
            'apellido'              :   forms.TextInput(attrs={'class':'form-control'}),
            'fechanacimiento'       :   forms.TextInput(attrs={'class':'form-control'}),
            'correoelectronico'     :   forms.TextInput(attrs={'class':'form-control'}),
            'celular'               :   forms.TextInput(attrs={'class':'form-control'}),
            'fk_genero'             :   forms.Select(attrs={'class':'form-control'}),         
        }

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascotas

        fields=[
            'nombre'            ,
            'fechanacimiento'   ,       
            'fk_especie'        ,
            'fk_raza'           ,
            'fk_generomascota'  ,
            'foto',
        ]

        labels={
            'nombre'            :   'nombre',
            'fechanacimiento'   :   'fechanacimiento',       
            'fk_especie'        :   'Especie',
            'fk_raza'           :   'Raza',
            'fk_generomascota'  :   'Genero',  
            'foto'                      :    'foto',           
        }

        widgets={
            'nombre'            :    forms.TextInput(attrs={'class':'form-control'}),
            'fechanacimiento'   :    forms.TextInput(attrs={'class':'form-control'}),
            'fk_especie'        :    forms.Select(attrs={'class':'form-control'}),   
            'fk_raza'           :    forms.Select(attrs={'class':'form-control'}),   
            'fk_generomascota'  :    forms.Select(attrs={'class':'form-control'}),   
            'foto'                      :   forms.FileInput()
      
        }

class ProductoForm(forms.ModelForm):

    class Meta:
        model =Producto

        fields=[
            'nombre',
            'fk_Tipoproducto',
            

        ]      

        labels={
            'nombre'            :   'nombre',
            'fk_Tipoproducto'   :   'tipo producto',
            
        }

        widgets={
            'nombre'            :   forms.TextInput(attrs={'class':'form-control'}),
            'fk_Tipoproducto'   :   forms.Select(attrs={'class':'form-control'}),   
        }

class InfoDesparacitacionForm(forms.ModelForm):
    def __init__(self ,id,*args, **kwargs):
        super(InfoDesparacitacionForm, self).__init__(*args, **kwargs)
        
        self.fields['fk_producto'].queryset =  Producto.objects.filter(fk_Tipoproducto=id[0].id)

    class Meta:
    
        model=InfoDesparacitacion

        fields=[
            'proximadesparacitante',
            'fk_producto',
            
        ]
        

        labels={
            'proximadesparacitante'     :   'proximadesparacitante',
            'fk_producto'               :   'Producto',
            
            
        }
        
        
        
        widgets={
            'proximadesparacitante'     :   forms.TextInput(attrs={'class':'form-control'}),
            'fk_producto'               :   forms.SelectMultiple(),
            
            

        }


class InfoVacunasForm(forms.ModelForm):
    def __init__(self, id, *args, **kwargs):
        super(InfoVacunasForm, self).__init__(*args, **kwargs)
        self.fields['fk_producto'].queryset =  Producto.objects.filter(fk_Tipoproducto=id[0].id)


    
    class Meta:
    
        model=InfoVacunas

        fields=[
            'proximavacuna',
            'fk_producto',
            'numeroregistro',
            


        ]
        

        labels={
            'proximavacuna'             :   'proxima vacuna',
            'fk_producto'               :   'Producto',
            'numeroregistro'            :    'numeroregistro',
            
        }
        
        
        widgets={
            'proximavacuna'             :   forms.TextInput(attrs={'class':'form-control'}),
            'fk_producto'               :   forms.Select(),
            'numeroregistro'            :   forms.TextInput(attrs={'class':'form-control'}),
            

        }




