from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente
from django.views.generic import ListView
from .forms import ConferenciaForm, EventoForm, PonenteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

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



@login_required
def create_conferencia(request):
    form = ConferenciaForm()
    if request.method == 'POST':
        form = ConferenciaForm(request.POST)
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
        form = ConferenciaForm(request.POST, instance=conferencia)
        if form.is_valid():
            form.save()
            return redirect('/ponencias')

    context = {'form':form}
    return render(request,"ponencia_form.html", context)

@login_required
def delete_conferencia(request,conferencia_id):
    conferencia = Conferencia.objects.get(id=conferencia_id)
    conferencia.delete()
    return redirect("/ponencias")

def Inicio(request):
    return render(request, 'index.html')

def detalles_evento(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    return render(request,'eventos/detalles_evento.html',{'evento':evento})

def detalles_ponente(request, id_ponente):
    ponente = get_object_or_404(Ponente, pk=id_ponente)
    return render(request,'ponentes/detalles_ponente.html',{'ponente':ponente})

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

@login_required
def editar_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    form = EventoForm(instance=evento)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('/eventos/'+str(evento_id))

    context = {'form':form}
    return render(request, "formulario_evento.html", context)

@login_required
def eliminar_evento(request,evento_id):
    evento = Evento.objects.get(id=evento_id)
    evento.delete()
    return redirect("/eventos")


@login_required
def crear_ponente(request):
    form = PonenteForm()
    if request.method == 'POST':
        form = PonenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ponentes/')
    context ={'form':form}
    return render(request, "formulario_ponente.html", context)

@login_required
def editar_ponente(request, ponente_id):
    ponente = Ponente.objects.get(id=ponente_id)
    form = PonenteForm(instance=ponente)

    if request.method == 'POST':
        form = PonenteForm(request.POST, instance=ponente)
        if form.is_valid():
            form.save()
            return redirect('/ponentes/'+str(ponente_id))

    context = {'form':form}
    return render(request, "formulario_ponente.html", context)

@login_required
def eliminar_ponente(request,ponente_id):
    ponente = Ponente.objects.get(id=ponente_id)
    ponente.delete()
    return redirect("/ponentes")