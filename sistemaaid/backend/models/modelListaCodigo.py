from django.db import models

class ListaCodigo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=280, null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaUltimaModificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    