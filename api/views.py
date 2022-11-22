from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente
from django.views.generic import ListView
from .forms import ConferenciaForm
from django.contrib.auth.decorators import login_required
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



@login_required
def create_conferencia(request):
    form = ConferenciaForm()
    if request.method == 'POST':
        form = ConferenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/ponencias')
    context ={'form':form}
    return render(request,"ponencia_form.html", context)
        
@login_required
def update_conferencia(request, conferencia_id):
    conferencia = Conferencia.objects.get(id=conferencia_id)
    form = ConferenciaForm(instance=conferencia)

    if request.method == 'POST':
        form = ConferenciaForm(request.POST, request.FILES, instance=conferencia)
        if form.is_valid():
            form.save()
            return redirect('/ponencias')

    context = {'form':form}
    return render(request,"ponencia_form.html", context)

@login_required
def delete_conferencia(request,conferencia_id):
    conferencia = Conferencia.objects.get(id=conferencia_id)
    context = {'producto':conferencia}
    conferencia.delete()
    return render(request, "ponencia_delete.html",context)

def Inicio(request):
    return render(request, 'index.html')

def detalles_evento(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    return render(request,'eventos/detalles_evento.html',{'evento':evento})
