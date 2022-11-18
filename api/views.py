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


def Inicio(request):
    return render(request, 'index.html')

def detalles_evento(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    return render(request,'eventos/detalles_evento.html',{'evento':evento})

def get_edicion_evento(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    return render(request,'eventos/edicion_evento.html',{'evento':evento})

def editar_evento(request, id_evento):
        evento= get_object_or_404(Evento, id=id_evento)
        if request.method == 'POST':
            if request.POST.get('form-titulo'):
                Evento.objects.filter(id = id_evento).update(titulo = request.POST.get('form-titulo'))
            if request.POST.get('form-descripcion'):
                Evento.objects.filter(id = id_evento).update(descripcion = request.POST.get('form-descripcion'))
            messages.success(request, "The post was successfully updated")
            return render(request, 'templates/detalles_evento.html')  
        else:
            context={'evento': evento,'error': 'The post was not successfully updated. The title and content must be filled out.'}
            return render(request,'templates/edicion_evento.html', context)