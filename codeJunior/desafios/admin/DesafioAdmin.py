from django.contrib import admin

from desafios.models import Desafio
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Desafio)
class DesafioAdmin(SummernoteModelAdmin):
    list_display = ('id','titulo','dificuldade','estimativa','ordem','ativo')
    search_fields = ('id', 'titulo','dificuldade')
    ordering = ('id',)
    summernote_fields=('descricao')