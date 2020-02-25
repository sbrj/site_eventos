from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.nome

class Evento(models.Model):
    show = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=False)
    descricao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='img_evento/', blank=True)


    class Meta:
        verbose_name_plural = "Eventos"

    @property 
    def mes_ano(self):
        data_evento = str(self.data.strftime('%d')) + '/' + str(self.data.strftime('%b'))
        return data_evento

    def __str__(self):
        return self.show

class Email(models.Model):
    email_f = models.EmailField(blank=True) 

    class Meta:
        verbose_name_plural = "emails"

    def __str__(self):
        return self.email_f

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    imagem = models.ImageField(upload_to='img_post/', blank=True)


    class Meta:
        verbose_name_plural = "posts"

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo