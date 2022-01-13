from django.db import models
from .modelEdicion import *
from django.db.models.deletion import CASCADE

class Metodologia(models.Model):
    descripcionCualitativa = models.CharField(max_length=280, null=True, blank=True)
    modalidadCualitativa = models.CharField(max_length=50,null=True, blank=True)
    descripcionCuantitativa = models.CharField(max_length=280, null=True, blank=True)
    modalidadCuantitativa = models.CharField(max_length=50,null=True, blank=True)
    edicionId =models.ForeignKey(Edicion, on_delete=CASCADE, null=True, blank=True)
