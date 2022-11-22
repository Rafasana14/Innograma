from django.forms import ModelForm
from .models import Conferencia


class ConferenciaForm(ModelForm):
    class Meta:
        model = Conferencia
        fields = '__all__'