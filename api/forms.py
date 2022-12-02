from django import forms
from .models import Evento, Conferencia, Ponente

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

class ConferenciaForm(forms.ModelForm):
    class Meta:
        model = Conferencia
        fields = '__all__'
        widgets = {
            'ponente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ponente de la conferencia'}),
            'tema': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tema de la conferencia'}),
            'fecha': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'yyyy-MM-dd HH:mm:ss'}),
            'espacio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Espacio reservado para la conferencia'}),
            'aforo_max': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Aforo máximo de la conferencia'}),
            'n_asistentes': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nº de asistentes de la conferencia'})
        }


class PonenteForm(forms.ModelForm):
    class Meta:
        model = Ponente
        fields = ['nombre', 'apellidos', 'especialidades', 'empresa', 'correo', 'telefono', 'otras_formas_de_contacto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del ponente'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos del ponente'}),
            'especialidades': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Especialidades del ponete'}),
            'empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa a la que pertenece'}),
            'correo': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@gmail.com'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono de contacto'}),
            'otras_formas_de_contacto': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Otras formas de contacto'})
        }
