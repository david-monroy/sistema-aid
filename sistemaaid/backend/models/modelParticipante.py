from django.db import models
from django.db.models.deletion import CASCADE
from .modelCarrera import *
from .modelColegio import *

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, null=True, blank=True)
    cedula = models.CharField(max_length=9, unique=True)
    correo = models.CharField(max_length=50, null=True, blank=True, unique=True)
    correoUcab = models.CharField(max_length=50, null=True, blank=True, unique=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    telfPrincipal = models.CharField(max_length=15)
    telfSecundario = models.CharField(max_length=15, null=True, blank=True)
    carreras = models.ManyToManyField(Carrera, through='ParticipanteCarrera')
    colegio = models.ForeignKey(Colegio, on_delete=CASCADE, null=True, blank=True)