from django.db import models
from django.db.models.deletion import CASCADE
from .modelCarrera import *
from .modelParticipante import *
from .modelSede import *

class ParticipanteCarrera(models.Model):
    participante = models.ForeignKey(Participante, on_delete=CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=CASCADE)
    sede = models.ForeignKey(Sede, on_delete=CASCADE, null=True, blank=True)
    semestre = models.IntegerField(null=True, blank=True)
