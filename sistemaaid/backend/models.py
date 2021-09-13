from django.db import models

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    cedula = models.CharField(max_length=9)
    correo = models.CharField(max_length=50, null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    telfPrincipal = models.CharField(max_length=15)
    telfSecundario = models.CharField(max_length=15, null=True, blank=True)

