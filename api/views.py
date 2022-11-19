from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente
from django.views.generic import ListView

# Create your views here.


class ConferenciasView(ListView):
    template_name = 'ponencias.html'
    model = Conferencia
    paginate_by = 3
    context_object_name = 'conferencias'
    
class EventosView(ListView):
    template_name = 'eventos.html'
    model = Evento
    paginate_by = 3
    context_object_name = 'eventos'


def Inicio(request):
    return render(request, 'index.html')

