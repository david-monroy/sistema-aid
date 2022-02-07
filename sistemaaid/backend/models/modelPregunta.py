from django.db import models
from django.db.models.deletion import CASCADE


class Pregunta(models.Model):
    codigo = models.CharField(max_length=30)
    etiqueta = models.CharField(max_length=280)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre