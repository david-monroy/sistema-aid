from django.db import models
from django.db.models.deletion import CASCADE
from .modelCarrera import *
from .modelColegio import *

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, null=True, blank=True)
    cedula = models.CharField(max_length=9, unique=True)
    correo = models.CharField(max_length=50, null=True, blank=True, unique=True)
    correoUcab = models.CharField(max_length=50, null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    telfPrincipal = models.CharField(max_length=15)
    telfSecundario = models.CharField(max_length=15, null=True, blank=True)
    lugar = models.CharField(max_length=150, null=True, blank=True)
    instagram = models.CharField(max_length=30, null=True, blank=True)
    twitter = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.CharField(max_length=30, null=True, blank=True)
    tiktok = models.CharField(max_length=30, null=True, blank=True)
    carreras = models.ManyToManyField(Carrera, through='ParticipanteCarrera')
    colegio = models.ForeignKey(Colegio, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre