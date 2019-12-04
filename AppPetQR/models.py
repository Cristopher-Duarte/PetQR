from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


#-----DATA BASE-----#


class Veterinaria(models.Model):
    nombre = models.CharField(max_length=40)
    fecharegistro = models.DateField(auto_now_add = True)
    logo = models.CharField(max_length=40)
    correocoorporativo = models.CharField(max_length=40)
    estado=models.BooleanField(null=True, default=True)
    telefono = models.CharField(max_length=40)
    

    
    def __str__(self):
        return self.nombre


class Especie(models.Model):
    especie = models.CharField(max_length=40)

    def __str__(self):
        return self.especie

class Raza(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=40)
    

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class GeneroMascota(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


class Sticker(models.Model):
    url = models.CharField(max_length=40)
    lote = models.CharField(max_length=40)

    def __str__(self):
        return self.url


class Usuario(models.Model):
    documento = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechanacimiento =  models.DateField()
    fecharegistro = models.DateField(auto_now_add = True)
    correoelectronico = models.CharField(max_length=40)
    estado=models.BooleanField(null=True, default=True)
    celular = models.CharField(max_length=40)

    fk_veterinaria=models.ForeignKey('Veterinaria', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    foto = models.CharField(max_length=40)
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)




class MedicoVeterinaria(models.Model):
    documento = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechanacimiento =  models.DateField()
    fecharegistro = models.DateField(auto_now_add = True)
    correoelectronico = models.CharField(max_length=40)
    estado=models.BooleanField(null=True, default=True)
    celular = models.CharField(max_length=40)

    fk_veterinaria=models.ForeignKey('Veterinaria', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre


class Mascotas(models.Model):
    nombre = models.CharField(max_length=40)
    fechanacimiento =  models.DateField()
    fecharegistro = models.DateField(auto_now_add = True)
    estado=models.BooleanField(null=True, default=True)

    fk_especie = models.ForeignKey('Especie', on_delete=models.CASCADE)
    fk_raza = models.ForeignKey('Raza', on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    fk_generomascota = models.ForeignKey('GeneroMascota', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    fk_producto = models.ForeignKey('TipoProducto', on_delete=models.CASCADE)
    fk_veterinaria = models.ForeignKey('Veterinaria', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre




class RecetaMedicas(models.Model):
    fecharegistro = models.DateField(auto_now_add = True)


    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE)
    fk_medicoveterinario = models.ForeignKey('MedicoVeterinaria', on_delete=models.CASCADE)


    def __str__(self):
        return self.fecharegistro

class DetalleRecetaMedica(models.Model):


    descripcion = models.CharField(max_length=60)

    fk_recetamedica = models.ForeignKey('RecetaMedicas', on_delete=models.CASCADE)
    fk_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)


    def __str__(self):
        return self.fk_producto

class InfoVacunas(models.Model):

    fecharegistro = models.DateField(auto_now_add = True)
    proximavacuna =  models.DateField()


    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE)
    fk_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)


    def __str__(self):
        return self.fk_producto

class DetalleInfoVacunas(models.Model):
    nombre= models.CharField(max_length=60)
    fk_infovacuna = models.ForeignKey('InfoVacunas', on_delete=models.CASCADE)
    fk_sticker = models.ForeignKey('Sticker', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class InfoDesparacitacion(models.Model):
    
    fecharegistro = models.DateField(auto_now_add = True)
    proximadesparacitante =  models.DateField()


    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE)
    fk_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)


    def __str__(self):
        return self.fk_producto


class Recordatorios(models.Model):
    fk_mascota = models.ForeignKey('Mascotas', on_delete=models.CASCADE)
    fk_infovacuna = models.ForeignKey('InfoVacunas', on_delete=models.CASCADE)


class Notificaciones(models.Model):
    fk_recordatorios = models.ForeignKey('Recordatorios', on_delete=models.CASCADE)




    

class Permission(models.Model):

    class Meta:
        permissions=(
            ('is_usuario', _('Is Usuario')),
            ('is_admin', _('Is Admin')),
            ('is_medico', _('Is Medico'))

        )




