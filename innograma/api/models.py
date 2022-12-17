from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.urls import reverse
    

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500, default=None)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    aforo_max = models.PositiveIntegerField(default=None, null=True, blank=True)
    n_asistentes = models.PositiveIntegerField(default=None, null=True, blank=True)
    premio = models.CharField(max_length=255, null=True, blank=True)
    coste = models.FloatField(default=None, null=True, blank=True, validators=[MinValueValidator(0.0)])
    
    def get_absolute_url(self):
        url = reverse('detalles_evento', args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.titulo)+ " - " + str(self.fecha.time()))
    
    class Meta:
        ordering = ('pk', )
    
class Ponente(models.Model):
    nombre = models.CharField(max_length=255, default=None)
    apellidos = models.CharField(max_length=255, default=None)
    especialidades = models.CharField(max_length=255, default=None)
    empresa = models.CharField(max_length=255, default=None, null=True, blank=True)
    correo = models.EmailField(max_length=100,unique=True, default=None, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Utilice el siguiente formato: '+999999999'. Se permite introducir hasta 15 cifras.")
    telefono = models.CharField(validators=[phone_regex],unique=True, max_length=17, blank=True)
    otras_formas_de_contacto = models.TextField(max_length=500, default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos
    
    class Meta:
        ordering = ('pk', )

class Conferencia(models.Model):
    tema = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    espacio = models.CharField(max_length=100)
    aforo_max = models.IntegerField(default=None, null=True, blank=True)
    n_asistentes = models.IntegerField(default=None, null=True, blank=True)

    def __str__(self):
        return self.tema
    
    def get_absolute_url(self):
        url = reverse('detalles_ponencia', args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.tema)+ " - " + str(self.fecha.time()))
    
    class Meta:
        ordering = ('pk', )


class Ponente_Conferencia(models.Model):
    ponente = models.ForeignKey(Ponente, on_delete=models.CASCADE)
    conferencia = models.ForeignKey(Conferencia, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('ponente', 'conferencia',)
        ordering = ('pk', )

    def __str__(self):
        return self.ponente.nombre + " " + self.ponente.apellidos
    