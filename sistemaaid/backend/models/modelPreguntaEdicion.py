from django.db import models
from django.db.models.deletion import CASCADE
from .modelPregunta import * 
from .modelEdicion import *

class PreguntaEdicion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=CASCADE)
    edicion = models.ForeignKey(Edicion, on_delete=CASCADE)

    def __str__(self):
        return self.pregunta