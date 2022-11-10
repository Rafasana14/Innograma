from django.shortcuts import render
from .models import Conferencia, Evento, Ponente


# Create your views here.

def get_all_conferencias(request):
    conferencias = Conferencia.objects.all()
    return render(request, 'ponencias.html', {'conferencias': conferencias})
