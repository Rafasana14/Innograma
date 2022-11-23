from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib import messages

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

class PonentesView(ListView):
    template_name = 'ponentes.html'
    model = Ponente
    paginate_by = 3
    context_object_name = 'ponentes'

def get_conferencia(request, conferencia_id):
    context = {
        'conferencia': Conferencia.objects.get(id=conferencia_id),
    }
    return render(request, "detalles_ponencia.html", context)


def Inicio(request):
    return render(request, 'index.html')

def detalles_evento(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    return render(request,'eventos/detalles_evento.html',{'evento':evento})