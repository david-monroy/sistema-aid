from django.db import models
from .modelEdicion import *
from django.db.models.deletion import CASCADE

class MuestraPonderada(models.Model):
    primeraCondicion = models.CharField(max_length=280)
    segundaCondicion = models.CharField(max_length=280)
    poblacion = models.IntegerField()
    muestra = models.IntegerField()
    edicion =models.ForeignKey(Edicion, on_delete=CASCADE, null=True, blank=True)


    def __str__(self):
        return self.primeraCondicion