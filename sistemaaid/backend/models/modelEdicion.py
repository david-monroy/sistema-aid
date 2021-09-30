from django.db import models
from .modelEstudio import *
from django.db.models.deletion import CASCADE

class Edicion(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    periodo = models.CharField(max_length=10)
    vinculada = models.BooleanField()
    totalMuestra = models.IntegerField()
    estudio =models.ForeignKey(Estudio, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.codigo