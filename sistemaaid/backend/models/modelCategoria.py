from django.db import models
from backend.models.modelListaCodigo import ListaCodigo
from django.db.models.deletion import CASCADE

class Categoria(models.Model):
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=280)
    listaCodigo =models.ForeignKey(ListaCodigo, on_delete=CASCADE, null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaUltimaModificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        unique_together = ('codigo', 'listaCodigo',)