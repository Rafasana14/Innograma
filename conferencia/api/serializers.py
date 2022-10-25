from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from conferencia.models import Conferencia

class ConferenciaSerializer(ModelSerializer):
    class Meta:
        model = Conferencia
        fields = ['id', 'ponente', 'tema', 'fecha', 'espacio', 'aforo_max', 'n_asistentes']