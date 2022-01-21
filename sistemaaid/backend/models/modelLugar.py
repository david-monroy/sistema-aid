from django.db import models
from django.db.models.deletion import CASCADE
from .modelLugar import *


class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fk_lugar = models.ForeignKey('self', on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre