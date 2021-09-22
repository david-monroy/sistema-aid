from django.db import models
from django.db.models.deletion import CASCADE


class Colegio(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField(null=False)