from django.contrib import admin
from .models import Noticia, Boletim


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')


@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
