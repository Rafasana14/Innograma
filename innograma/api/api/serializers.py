from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from api.models import Conferencia, Evento, Ponente

class ConferenciaSerializer(ModelSerializer):
    class Meta:
        model = Conferencia
        fields = ['id', 'ponente', 'tema', 'fecha', 'espacio', 'aforo_max', 'n_asistentes']
        
class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'titulo', 'descripcion','fecha', 'lugar', 'aforo_max', 'n_asistentes', 'premio', 'coste']
        
class PonenteSerializer(ModelSerializer):
    class Meta:
        model = Ponente
        fields =  ['nombre', 'apellidos', 'especialidades', 'conferencias_impartidas', 'empresa', 'correo', 'telefono', 'otras_formas_de_contacto']