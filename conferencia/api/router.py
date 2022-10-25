from email.mime import base
from rest_framework.routers import DefaultRouter
from conferencia.api.views import ConferenciaApiViewSet

router_conferencias = DefaultRouter()

router_conferencias.register(prefix='conferencia', basename='conferencia', viewset=ConferenciaApiViewSet)