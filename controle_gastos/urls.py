"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings        
from django.conf.urls.static import static
from contas.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem, name='todos_eventos'),
    path('evento/novo/', novo_evento, name='novo_even'),
    path('update/<str:id>/', update, name='atualizar'),
    path('delete/<str:id>/', delete, name='deletar'),
    path('posts/', postagens, name='postagens'),
    path('post/<str:id>/', post, name='post'),
    path('post/novo', novo_post, name="novo_post"),
    path('post/<str:id>/editar/', editar_post, name='editar_post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
