from django.contrib import admin
from api.models import Conferencia, Evento, Ponente, Ponente_Conferencia


@admin.register(Conferencia)
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'tema', 'fecha', 'espacio', 'aforo_max', 'n_asistentes']
    #filter_horizontal = ('ponente',)
    
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descripcion', 'fecha', 'lugar', 'aforo_max', 'n_asistentes', 'premio', 'coste']
    
@admin.register(Ponente)
class PonenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'especialidades', 'empresa', 'correo', 'telefono', 'otras_formas_de_contacto']

@admin.register(Ponente_Conferencia)
class Ponente_ConferenciaAdmin(admin.ModelAdmin):
    list_display = ['ponente', 'conferencia']
