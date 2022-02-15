from django.db import models
from django.db.models.deletion import CASCADE
from .modelListaCodigo import *


class Pregunta(models.Model):
    codigo = models.CharField(max_length=30)
    etiqueta = models.CharField(max_length=280)
    tipo = models.CharField(max_length=30)
    listaCodigo = models.ForeignKey(ListaCodigo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre