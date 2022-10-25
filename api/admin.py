from django.contrib import admin
from api.models import Conferencia, Evento, Ponente


@admin.register(Conferencia)
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ponente', 'tema', 'fecha', 'espacio', 'aforo_max', 'n_asistentes']
    
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descripcion', 'fecha', 'lugar', 'aforo_max', 'n_asistentes', 'premio', 'coste']
    
@admin.register(Ponente)
class PonenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'especialidades', 'conferencias_impartidas', 'empresa', 'correo', 'telefono', 'otras_formas_de_contacto']
