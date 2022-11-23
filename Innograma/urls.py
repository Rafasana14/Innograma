"""Innograma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from api.api.router import router_api
from api import views
from api.views import Inicio, PonentesView, ConferenciasView, EventosView, detalles_evento, crear_evento, editar_evento, eliminar_evento, get_conferencia, create_conferencia, update_conferencia, delete_conferencia


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router_api.urls)),
    path('eventos/<int:id_evento>', views.detalles_evento, name="detalles_evento"),
    path("ponencias/",views.ConferenciasView.as_view(),name="ponencias"),
    path("ponencias/<int:conferencia_id>",views.get_conferencia,name="conferencia"),
    path("ponencias/crear",views.create_conferencia,name="crear_ponencia"),
    path("ponencias/<int:conferencia_id>/editar",views.update_conferencia, name="editar_conferencia"),
    path("ponencias/<int:conferencia_id>/eliminar",views.delete_conferencia, name="eliminar_conferencia"),
    path("ponentes/",views.PonentesView.as_view(),name="ponentes"),
    path("ponentes/<int:id_ponente>",views.detalles_ponente,name="detalles_ponente"),
    path("eventos/",views.EventosView.as_view(),name="eventos"),
    path("eventos/crear",views.crear_evento, name="crear_evento"),
    path("eventos/<int:evento_id>/editar",views.editar_evento, name="editar_evento"),
    path("eventos/<int:evento_id>/eliminar",views.eliminar_evento, name="eliminar_evento"),
    path("",views.Inicio, name="index"),
]
