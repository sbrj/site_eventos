from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Evento, Email, Post
from .forms import EventoForm, EmailForm, PostForm
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
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForm(request.POST or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('todos_eventos')
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
    data['email_html'] = email_f(request.POST)  
    search = request.GET.get('search')
    if search:
        data['eventos'] = Evento.objects.filter(show__icontains=search)
    else:
        data['eventos'] = Evento.objects.all().order_by('data')
    return render(request, 'contas/listagem.html', data)

def postagens(request):
    data ={}
    data['posts'] = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('-data_publicacao')
    data['email_html'] = email_f(request.POST)
    return render(request, 'contas/postagens.html', data)

def post(request, id):
    data = {}
    artigo = get_object_or_404(Post, pk=id)
    data['email_html'] = email_f(request.POST)
    data['post'] = artigo
    return render(request, 'contas/post.html', data)

def novo_post(request):
    email = email_f(request.POST)
    if request.method == "POST":
        n_post = PostForm(request.POST)
        if n_post.is_valid():
            post = n_post.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('novo_post')
    else:
        n_post = PostForm()
    return render(request, 'contas/editar_post.html', {'form_post_html': n_post, 'email_html': email})

def editar_post(request, id):
    post = get_object_or_404(Post, pk=id)
    email = email_f(request.POST)
    if request.method == "POST":
        n_post = PostForm(request.POST, instance=post)
        if n_post.is_valid():
            post = n_post.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post', post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'contas/editar_post.html', {'form_post_html': form, 'post': post, 'email_html': email})

def email_f(request):
    email_form = EmailForm(request or None)
    if email_form.is_valid():
        email_form.save()
    return email_form