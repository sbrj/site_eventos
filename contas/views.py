from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Evento, Email, Post
from .forms import EventoForm, EmailForm
import datetime

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
        return redirect('/todos_eventos')
    data['form'] = form
    data['evento'] = evento
    data['email_html'] = email_f(request.POST) 
    return render(request, 'contas/form.html', data)

def delete(request, id):
    evento = Evento.objects.get(pk=id)
    evento.delete()
    return redirect('todos_eventos')

def listagem(request):
    data = {}
    data['eventos'] = Evento.objects.all()
    data['email_html'] = email_f(request.POST)  
    return render(request, 'contas/listagem.html', data)

def postagens(request):
    data ={}
    data['posts'] = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    data['email_html'] = email_f(request.POST)
    return render(request, 'contas/postagens.html', data)

def email_f(request):
    email_form = EmailForm(request or None)
    if email_form.is_valid():
        email_form.save()
    return email_form