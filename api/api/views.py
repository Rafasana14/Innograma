from rest_framework.viewsets import ModelViewSet
from api.models import Conferencia, Evento, Ponente
from api.api.serializers import ConferenciaSerializer, EventoSerializer, PonenteSerializer

class ConferenciaApiViewSet(ModelViewSet):
    serializer_class = ConferenciaSerializer
    queryset = Conferencia.objects.all()

class EventoApiViewSet(ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    
class PonenteApiViewSet(ModelViewSet):
    serializer_class = PonenteSerializer
    queryset = Ponente.objects.all()