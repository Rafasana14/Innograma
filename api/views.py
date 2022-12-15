from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.core.paginator import Paginator
from .models import Conferencia, Evento, Ponente, Ponente_Conferencia
from django.views.generic import ListView
from .forms import ConferenciaForm, EventoForm, Ponente_ConferenciaForm, PonenteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
import datetime
import calendar
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from .CalendarioEventos import CalendarioEventos

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
    conferencia = get_object_or_404(Conferencia,pk=conferencia_id)
    ponentesAux = Ponente_Conferencia.objects.filter(conferencia = conferencia)
    ponentes = []
    for ponente in ponentesAux:
        ponentes.append(ponente.ponente)
    context = {
        'conferencia': conferencia,
        'ponentes': ponentes,
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
def ponente_conferencia(request, conferencia_id):
    conferencia = get_object_or_404(Conferencia, id=conferencia_id)
    ponentes =  Ponente_Conferencia.objects.filter(conferencia = conferencia).values_list('ponente')
    ids = []
    for it in ponentes:
        ids.append(it[0])
    form = Ponente_ConferenciaForm()
    form.fields['ponente'].queryset = Ponente.objects.all().exclude(id__in = ids)
    if request.method == 'POST':
        form = Ponente_ConferenciaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ponente = cd['ponente']
            Ponente_Conferencia.objects.create(conferencia=conferencia, ponente = ponente)
            return redirect('/ponencias')
    context ={'form':form, 'conferencia':conferencia}
    return render(request,"ponente_ponencia_form.html", context)

@login_required
def delete_ponente_conferencia(request, conferencia_id):
    conferencia = get_object_or_404(Conferencia, id=conferencia_id)
    ponentes =  Ponente_Conferencia.objects.filter(conferencia = conferencia).values_list('ponente')
    ids = []
    for it in ponentes:
        ids.append(it[0])
    form = Ponente_ConferenciaForm()
    form.fields['ponente'].queryset = Ponente.objects.all().filter(id__in = ids)
    if request.method == 'POST':
        form = Ponente_ConferenciaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ponente = cd['ponente']
            Ponente_Conferencia.objects.filter(conferencia=conferencia, ponente = ponente).delete()
            return redirect('/ponencias')
    context ={'form':form, 'conferencia':conferencia}
    return render(request,"ponente_ponencia_form_delete.html", context)

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
    conferenciasAux = Ponente_Conferencia.objects.filter(ponente = ponente)
    conferencias = []
    for conferencia in conferenciasAux:
        conferencias.append(conferencia.conferencia)
    context = {
        'conferencias': conferencias,
        'ponente': ponente,
    }
    return render(request,'ponentes/detalles_ponente.html', context)

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

def calendario(request):
    month = request.GET.get('mes', None)
    year = request.GET.get('año', datetime.date.today().year)
    message=""

    if month == None:
        eventos_year = Evento.objects.filter(fecha__year=year)
        print(eventos_year.count())
        if(len(eventos_year)==0):
            eventos_year = Conferencia.objects.filter(fecha__year=year)
        if(len(eventos_year)==0):
            message = "No hay eventos o conferencias en ese año. Mostrando enero."
            month = 1
        else:
            month = eventos_year[0].fecha.month
    if year == None:
        message = "No hay eventos o conferencias en ese año. Mostrando semana actual."
        d = datetime.date.today()
    else:
        try:
            if(eventos_year.count()==0):
                d = datetime.date(year=int(year), month=int(month), day=1)
            else:    
                d = datetime.date(year=int(year), month=int(month), day=eventos_year[0].fecha.day)
        except:
            d = datetime.date.today()

    '''previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
    previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
    previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                    day=1)  # find first day of previous month

    last_day = calendar.monthrange(d.year, d.month)
    next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
    next_month = next_month + datetime.timedelta(days=1)  # forward a single day
    next_month = datetime.date(year=next_month.year, month=next_month.month,
                                day=1)  # find first day of next month'''
    
    first_day = d.weekday()
    first_day = datetime.timedelta(days=first_day)
    first_day = d - first_day
    week = []
    for i in range(7):
        delta = datetime.timedelta(days=i)
        dia=first_day+delta
        week.append((dia.day,dia.weekday()))
    years=[]
    fecha_aux=datetime.date.today()
    for i in range(10):
        delta = datetime.timedelta(days=365*i)
        aux=fecha_aux-delta
        years.append(aux.year)
        
    for i in range(1,10):
        delta = datetime.timedelta(days=365*i)
        aux=fecha_aux+delta
        years.append(aux.year)
    years.sort()

    cal = CalendarioEventos()
    #html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
    #html_calendar = cal.formatweek(week)
    # html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
    v = []
    a = v.append
    a('<table border="0" cellpadding="0" cellspacing="0" class="%s">' % (cal.cssclass_month))
    a('\n')
    a(cal.formatmonthname(d.year, d.month, withyear=True))
    a('\n')
    a(cal.formatweekheader())
    a('\n')
    a(cal.formatweek(week,d.year))
    a('\n')
    a('</table>')
    a('\n')
    html_calendar = ''.join(v)
    html_calendar = html_calendar.replace('<td ', '<td  width="180" height="150"')
    
    context = {
        'calendario': mark_safe(html_calendar),
        'years': years,
        'current_year': d.year,
        'message': message,
    }
    '''next_month': next_month.month,
        'next_year': next_month.year,
        'previous_month': previous_month.month,
        'previous_year': previous_month.year,'''
    
    return render(request, "calendario/calendario.html", context)