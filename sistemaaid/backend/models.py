from django.db import models
from django.db.models.deletion import CASCADE

class Carrera(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=20)
    estaEnUCAB = models.BooleanField()

class Sede(models.Model):
    nombre = models.CharField(max_length=30)

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    cedula = models.CharField(max_length=9)
    correo = models.CharField(max_length=50, null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    telfPrincipal = models.CharField(max_length=15)
    telfSecundario = models.CharField(max_length=15, null=True, blank=True)
    carreras = models.ManyToManyField(Carrera, through='ParticipanteCarrera')

class ParticipanteCarrera(models.Model):
    participante = models.ForeignKey(Participante, on_delete=CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=CASCADE)
    sede = models.ForeignKey(Sede, on_delete=CASCADE, null=False, blank=False)
    semestre = models.IntegerField(null=True, blank=True)
    esEgresado = models.BooleanField(null=True, blank=True)