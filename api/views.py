from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventoForm

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


def Inicio(request):
    return render(request, 'index.html')

def detalles_evento(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    return render(request,'eventos/detalles_evento.html',{'evento':evento})

@login_required
def crear_evento(request):
    form = EventoForm()
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/eventos/')
    context ={'form':form}
    return render(request, "formulario_evento.html", context)