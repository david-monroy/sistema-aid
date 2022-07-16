from django.db import models
from .modelParticipante import *
from django.db.models.deletion import CASCADE

class Encuesta(models.Model):
    fechaAplicacion = models.DateField()
    estaCodificada = models.BooleanField(default=False)
    codigo = models.IntegerField()
    participante =models.ForeignKey(Participante, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.participante