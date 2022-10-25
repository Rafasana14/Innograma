from rest_framework.viewsets import ModelViewSet
from conferencia.models import Conferencia
from conferencia.api.serializers import ConferenciaSerializer

class ConferenciaApiViewSet(ModelViewSet):
    serializer_class = ConferenciaSerializer
    queryset = Conferencia.objects.all()