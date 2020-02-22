from django.forms import ModelForm, TextInput
from .models import Evento, Email, Post

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

class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Digite o título'}),
            'texto': TextInput(attrs={'placeholder': 'Digite o texto desejado aqui'}),
        }
        fields = ['title', 'texto']
        