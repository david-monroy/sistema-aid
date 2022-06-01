from django.db import models
from django.db.models.deletion import CASCADE

class Carrera(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField(null=False)
    estaEnUCAB = models.BooleanField()

    def __str__(self):
        return self.nombre
