from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Evento, Conferencia
 
 
class CalendarioEventos(HTMLCalendar):
    def __init__(self, eventos=None, conferencias= None):
        super(CalendarioEventos, self).__init__()
        self.eventos = eventos
        self.conferencias = conferencias
 
    def formatday(self, day, weekday, eventos, conferencias):
        """
        Return a day as a table cell.
        """
        eventos_from_day = eventos.filter(fecha__day=day)
        conferencias_from_day = conferencias.filter(fecha__day=day)
        html=""
        eventos_html=""
        conferencias_html=""
        if(eventos_from_day.count()!=0):    
            eventos_html = "<ul>"
            for evento in eventos_from_day:
                eventos_html += evento.get_absolute_url() + "<br>"
            eventos_html += "</ul>"
        if(conferencias_from_day.count()!=0):
            conferencias_html = "<ul>"
            for conferencia in conferencias_from_day:
                conferencias_html += conferencia.get_absolute_url() + "<br>"
            conferencias_html += "</ul>"
        html = eventos_html+conferencias_html
 
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, html)
 
    def formatweek(self, theweek, year):
        """
        Return a complete week as a table row.
        """
        eventos = Evento.objects.filter(fecha__year=year)
        conferencias = Conferencia.objects.filter(fecha__year=year)
        s = ''.join(self.formatday(d, wd, eventos, conferencias) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s