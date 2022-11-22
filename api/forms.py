from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título del evento'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripción detallada del evento'}),
            'fecha': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'yyyy-MM-dd HH:mm:ss'}),
            'lugar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lugar del evento'}),
            'aforo_max': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Aforo máximo del evento'}),
            'n_asistentes': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nº de asistentes del evento'}),
            'premio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Premios del evento'}),
            'coste': forms.NumberInput(attrs={'class':'form-control','step':"0.01", 'placeholder':'Coste del evento (en euros)'})
        }