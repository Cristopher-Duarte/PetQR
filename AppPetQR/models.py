from django.db import models

#-----DATA BASE-----#


class Veterinaria(models.model):
    nombre = models.CharField(max_lenght=40)
    fecharegistro = models.DataField(auto_now_add = True)
    logo = models.CharField(max_lenght=40)
    correocoorporativo = models.CharField(max_lenght=40)
    estado=models.BooleanField(null=True, default=True)
    telefono = models.CharField(max_lenght=40)
    

    
    def __str__(self):
        return self.nombre


class Especie(models.model):
    especie = models.CharField(max_lenght=40)

    def __str__(self):
        return self.especie

class Raza(models.model):
    nombre = models.CharField(max_lenght=40)

    def __str__(self):
        return self.nombre


class TipoProducto(models.model):
    nombre = models.CharField(max_lenght=40)
    

    def __str__(self):
        return self.nombre


class Genero(models.model):
    nombre = models.CharField(max_lenght=40)

    def __str__(self):
        return self.nombre

class GeneroMascota(models.model):
    nombre = models.CharField(max_lenght=40)

    def __str__(self):
        return self.nombre


class Sticker(models.model):
    url = models.CharField(max_lenght=40)

    def __str__(self):
        return self.url


class Usuario(models.model):
    documento = models.CharField(max_lenght=40)
    nombre = models.CharField(max_lenght=40)
    apellido = models.CharField(max_lenght=40)
    fechanacimiento =  models.DataField()
    fecharegistro = models.DataField(auto_now_add = True)
    correoelectronico = models.CharField(max_lenght=40)
    estado=models.BooleanField(null=True, default=True)
    celular = models.CharField(max_lenght=40)

    fk_veterinaria=models.ForeignKet('Veterinaria', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre



class MedicoVeterinaria(models.model):
    documento = models.CharField(max_lenght=40)
    nombre = models.CharField(max_lenght=40)
    apellido = models.CharField(max_lenght=40)
    fechanacimiento =  models.DataField()
    fecharegistro = models.DataField(auto_now_add = True)
    correoelectronico = models.CharField(max_lenght=40)
    estado=models.BooleanField(null=True, default=True)
    celular = models.CharField(max_lenght=40)

    fk_veterinaria=models.ForeignKet('Veterinaria', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre


class Mascotas(models.model):
    nombre = models.CharField(max_lenght=40)
    fechanacimiento =  models.DataField()
    fecharegistro = models.DataField(auto_now_add = True)
    estado=models.BooleanField(null=True, default=True)

    fk_especie = models.ForeignKet('Especie', on_delete=models.CASCADE)
    fk_raza = models.ForeignKet('Raza', on_delete=models.CASCADE)
    fk_usuario = models.ForeignKet('Usuario', on_delete=models.CASCADE)
    fk_generomascota = models.ForeignKet('GeneroMascota', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Producto(models.model):
    nombre = models.CharField(max_lenght=40)
    fk_producto = models.ForeignKet('TipoProducto', on_delete=models.CASCADE)
    fk_veterinaria = models.ForeignKet('Veterinaria', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre




class RecetaMedicas(models.model):
    fecharegistro = models.DataField(auto_now_add = True)


    fk_mascota = models.ForeignKet('Mascotas', on_delete=models.CASCADE)
    fk_medicoveterinario = models.ForeignKet('MedicoVeterinaria', on_delete=models.CASCADE)


    

class Permission(models.model):

    class Meta:
        permissions=(
            ('is_usuario', _('Is Usuario')),
            ('is_admin', _('Is Admin')),
            ('is_medico', _('Is Medico'))

        )




