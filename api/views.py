from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, HttpResponse

# Create your views here.


class ConferenciasView(ListView):
    template_name = 'ponencias.html'
    model = Conferencia
    paginate_by = 3
    context_object_name = 'conferencias'


def Inicio(request):
    return render(request, 'index.html')

def detalles_evento(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    return render(request,'detalles_evento.html',{'evento':evento})
