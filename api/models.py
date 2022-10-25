from django.db import models

class Conferencia(models.Model):
    ponente = models.CharField(max_length=100)
    tema = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    espacio = models.CharField(max_length=100)
    aforo_max = models.IntegerField(default=None, null=True, blank=True)
    n_asistentes = models.IntegerField(default=None, null=True, blank=True)
    

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500, default=None)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    aforo_max = models.IntegerField(default=None, null=True, blank=True)
    n_asistentes = models.IntegerField(default=None, null=True, blank=True)
    premio = models.CharField(max_length=255, null=True, blank=True)
    coste = models.FloatField(default=None, null=True, blank=True)
    
class Ponente(models.Model):
    nombre = models.CharField(max_length=255, default=None)
    apellidos = models.CharField(max_length=255, default=None)
    especialidades = models.CharField(max_length=255, default=None)
    conferencias_impartidas = models.TextField(max_length=500, default=None)
    empresa = models.CharField(max_length=255, default=None, null=True, blank=True)
    correo = models.EmailField(max_length=100, default=None, null=True, blank=True)
    telefono = models.CharField(max_length=12, default=None, null=True, blank=True) #Modificar para que verifique que son números
    otras_formas_de_contacto = models.TextField(max_length=500, default=None, null=True, blank=True)
    