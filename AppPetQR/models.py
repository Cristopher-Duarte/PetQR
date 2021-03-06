from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


#-----DATA BASE-----#


class Veterinaria(models.Model):
    nombre = models.CharField(max_length=40)
    fecharegistro = models.DateField(auto_now_add = True)
    logo = models.CharField(max_length=40)
    correocoorporativo = models.CharField(max_length=40)
    estado=models.BooleanField(default=True)
    telefono = models.CharField(max_length=40)
    

    
    def __str__(self):
        return self.nombre


class Especie(models.Model):
    
    especie = models.CharField(max_length=40)

    def __str__(self):
        return self.especie

class Raza(models.Model):
    
    
    nombre = models.CharField(max_length=40)
    fk_especie =models.ForeignKey('Especie', on_delete=models.CASCADE, db_column="fk_especie")

    def __str__(self):
        return self.nombre


class TipoProducto(models.Model):
    

    nombre = models.CharField(max_length=40)
    

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    fk_Tipoproducto = models.ForeignKey('TipoProducto', on_delete=models.CASCADE, db_column="fk_Tipoproducto")
    fk_veterinaria = models.ForeignKey('Veterinaria', on_delete=models.CASCADE, db_column="fk_veterinaria")


    def __str__(self):
        return self.nombre


class Genero(models.Model):
    
    nombre = models.CharField(max_length=40,  default=1)

    def __str__(self):
        return self.nombre

class GeneroMascota(models.Model):
    
    nombre = models.CharField(max_length=40, default=1)

    def __str__(self):
        return self.nombre




class Usuario(models.Model):
    documento = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechanacimiento =  models.DateField()
    
    fecharegistro = models.DateField(auto_now_add = True)
    correoelectronico = models.CharField(max_length=40)
    estado=models.BooleanField(default=True)
    celular = models.CharField(max_length=40)

    fk_veterinaria = models.ForeignKey('Veterinaria', on_delete=models.CASCADE, db_column="fk_veterinaria")
    fk_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column="fk_genero")


    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    foto = models.CharField(max_length=40)
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column="fk_usuario")




class MedicoVeterinaria(models.Model):
    documento = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechanacimiento =  models.DateField()
    fecharegistro = models.DateField(auto_now_add = True)
    correoelectronico = models.CharField(max_length=40)
    estado=models.BooleanField(default=True)
    celular = models.CharField(max_length=40)

    fk_veterinaria = models.ForeignKey('Veterinaria', on_delete=models.CASCADE, db_column="fk_veterinaria")
    fk_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column="fk_genero")


    def __str__(self):
        return self.nombre


class Mascotas(models.Model):
    nombre = models.CharField(max_length=40)
    fechanacimiento =  models.DateField()
    fecharegistro = models.DateField(auto_now_add = True)
    estado=models.BooleanField(default=True)

    foto=models.ImageField(upload_to='Images/%Y', null=True, blank=True)

    fk_especie = models.ForeignKey('Especie', on_delete=models.CASCADE, db_column="fk_especie")
    fk_raza = models.ForeignKey('Raza', on_delete=models.CASCADE, db_column="fk_raza")
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column="fk_usuario")
    fk_generomascota = models.ForeignKey('GeneroMascota', on_delete=models.CASCADE, db_column="fk_generomascota")
    
    def __str__(self):
        return self.nombre







class ControlesMedicos(models.Model):
    fecharegistro = models.DateField(auto_now_add = True)
    observacion = models.CharField(max_length= 250)
    proximadesControl = models.DateField()
    

    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE, db_column="fk_mascota")
    fk_medicoveterinario = models.ForeignKey('MedicoVeterinaria', on_delete=models.CASCADE, db_column="fk_medicoveterinario")


    
class DetalleRecetaMedica(models.Model):
    
    indicaciones = models.CharField(max_length=200)
    fk_ControlMedico = models.ForeignKey('ControlesMedicos', on_delete=models.CASCADE, db_column="fk_ControlMedico")
    fk_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column="fk_producto")


class InfoVacunas(models.Model):

    fecharegistro = models.DateField(auto_now_add = True)
    proximavacuna =  models.DateField()
    
    
    sticker = models.ImageField(upload_to='Images/%Y/%m/%d', null=True, blank=True)

    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE, db_column="fk_mascota")
    fk_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column="fk_producto")


class Efectos(models.Model):
    nombre = models.CharField(max_length=40)
    
    

    

class DetalleInfoVacunas(models.Model):
    fk_efecto = models.ForeignKey('Efectos', on_delete=models.CASCADE, db_column="fk_efecto")
    fk_infovacuna = models.ForeignKey('InfoVacunas', on_delete=models.CASCADE, db_column="fk_infovacuna")
    




class InfoDesparacitacion(models.Model):
    
    fecharegistro = models.DateField(auto_now_add = True)
    proximadesparacitante =  models.DateField()


    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE, db_column="fk_mascota")
    fk_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column="fk_producto")



class Recordatorios(models.Model):
    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE, db_column="fk_mascota")
    fk_infovacuna = models.ForeignKey('InfoVacunas', on_delete=models.CASCADE, db_column="fk_infovacuna")


class Notificaciones(models.Model):
    fk_recordatorios = models.ForeignKey('Recordatorios', on_delete=models.CASCADE, db_column="fk_recordatorios")




    

class Permission(models.Model):

    class Meta:
        permissions=(
            ('is_usuario', _('Is Usuario')),
            ('is_admin', _('Is Admin')),
            ('is_medico', _('Is Medico'))

        )