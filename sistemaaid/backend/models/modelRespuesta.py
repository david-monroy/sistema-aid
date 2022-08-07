from django.db import models

from backend.models.modelPreguntaEdicion import PreguntaEdicion
from .modelEncuesta import *
from django.db.models.deletion import CASCADE

class Respuesta(models.Model):
    respuesta = models.CharField(max_length=280)
    codigo = models.CharField(max_length=10,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta, on_delete=CASCADE)
    pregunta = models.ForeignKey(PreguntaEdicion, on_delete=CASCADE)

    def __str__(self):
        return self.respuesta