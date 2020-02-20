from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento, Email
from .forms import EventoForm, EmailForm
import datetime

def home(request):
    data = {} 
    data['eventos'] = ['ev1', 'ev2', 'ev3']

    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)

def novo_evento(request):
    data = {}
    form = EventoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('todos_eventos')
    data['form'] = form

    return render(request, 'contas/form.html', data)

def update(request, id):
    data = {}
    evento = Evento.objects.get(pk=id)
    form = EventoForm(request.POST or None, instance=evento)

    if form.is_valid():
        form.save()
        return redirect('todos_eventos')
    data['form'] = form
    data['evento'] = evento
    return render(request, 'contas/form.html', data)

def delete(request, id):
    evento = Evento.objects.get(pk=id)
    evento.delete()
    return redirect('todos_eventos')

def listagem(request):
    data = {}
    email_form = EmailForm(request.POST or None)
    data['eventos'] = Evento.objects.all()
    if email_form.is_valid():
        email_form.save()
        return redirect('todos_eventos')
    data['email_html'] = email_form    
    return render(request, 'contas/listagem.html', data)

def postagens(request):
    return render(request, 'contas/postagens.html', {})