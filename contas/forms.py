from django.forms import ModelForm, TextInput
from .models import Evento, Email

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['show', 'valor', 'categoria', 'data', 'descricao' ]

class EmailForm(ModelForm):
    class Meta:
        model = Email
        widgets = {
            'email_f': TextInput(attrs={'placeholder': 'Digite seu email'}),
        }
        fields = ['email_f']
        labels = {
            'email_f': (''),
            }
        