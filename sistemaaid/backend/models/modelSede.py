from django.db import models
from django.db.models.deletion import CASCADE


class Sede(models.Model):
    nombre = models.CharField(max_length=30)