from pyexpat import model
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models


class Conferencia(models.Model):
    ponente = models.CharField(max_length=100)
    tema = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    espacio = models.CharField(max_length=100)
    aforo_max = models.IntegerField(default=None)
    n_asistentes = models.IntegerField(default=None, null=True, blank=True)