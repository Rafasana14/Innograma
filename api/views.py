from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente
from django.views.generic import ListView
from .forms import ConferenciaForm
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



@login_required
def create_conferencia(request):
    form = ConferenciaForm()
    if request.method == 'POST':
        form = ConferenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request, "ponencia_form.html", context)
        

def Inicio(request):
    return render(request, 'index.html')



