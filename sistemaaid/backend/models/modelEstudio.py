from django.db import models

class Estudio(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    poblacionObjetivo = models.CharField(max_length=50)
    antecedentes = models.CharField(max_length=280, null=True, blank=True)
    objetivoNegocio = models.CharField(max_length=280)

    def __str__(self):
        return self.nombre