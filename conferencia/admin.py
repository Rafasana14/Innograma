from django.contrib import admin
from conferencia.models import Conferencia


@admin.register(Conferencia)
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ponente', 'tema', 'fecha', 'espacio', 'aforo_max', 'n_asistentes']