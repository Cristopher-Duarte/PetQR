from django.db import models

#-----DATA BASE-----#


class Veterinaria(models.model):
    nombre = models.CharField(max_lenght=40)
    
    def __str__(self):
        return self.nombre

class Usuario(models.model):
    veterinaria = models.ForeignKey('Veterinaria', on_delete=models.CASCADE)

class Mascotas(models.model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Recordatorios(models.model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    veterinaria = models.ForeignKey('Veterinaria', on_delete=models.CASCADE)

class Notificaciones(models.model):
    recordatorios = models.ForeignKey('Recordatorios', on_delete=models.CASCADE)


#-------------------------VACUNAS Y DESPARACITACIÓN-------------------------#


class InfoDesparacitacion(models.model):
    informacion = models.CharField(max_lenght=40)

    def __str__(self):
        return self.informacion

class Stickers(models.model):
    sticker = models.ImageField()

class InfoVacunas(models.model):
    stickers = models.ForeignKey('Stickers', on_delete=models.CASCADE)

class Detalle(models.model):
    mascotas = models.ForeignKey('Mascotas', on_delete=models.CASCADE)
    infovacunas = models.ForeignKey('InfoVacunas', on_delete=models.CASCADE)
    infodesparacitacion = models.ForeignKey('InfoDesparacitacion', on_delete=models,CASCADE)


#-------------------------CONTROLES MEDICOS-------------------------#


class MedicoVect(models.model):
    veterinaria = models.ForeignKey('Veterinaria', on_delete=models.CASCADE)

class RecetasMedicas(models.model):
    mascotas = models.ForeignKey('Mascotas', on_delete=models.CASCADE)
    medicovect = models.ForeignKey('MedicoVect', on_delete=models.CASCADE)

class DetalleReceta(models.model):
    recetasmedicas = models.ForeignKey('RecetasMedicas', on_delete=models.CASCADE)
    nombre = models.CharField(max_lenght=40)