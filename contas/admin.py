from django.contrib import admin
from .models import *

class EventosAdmin(admin.ModelAdmin):
    list_display = ('show', 'data', 'categoria', 'valor')

    def show_info(self, obj):
        return obj

admin.site.register(Categoria)
admin.site.register(Evento, EventosAdmin)
admin.site.register(Email)
admin.site.register(Post)
admin.site.site_header = 'Painel de Controle Beco das Garrafas'