from email.mime import base
from rest_framework.routers import DefaultRouter
from api.api.views import ConferenciaApiViewSet, EventoApiViewSet, PonenteApiViewSet

router_api = DefaultRouter()

router_api.register(prefix='conferencias', basename='conferencias', viewset=ConferenciaApiViewSet)
router_api.register(prefix='eventos', basename='eventos', viewset=EventoApiViewSet)
router_api.register(prefix='ponentes', basename='ponentes', viewset=PonenteApiViewSet)