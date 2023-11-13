from django.contrib import admin

from desafios.models import Trilha
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Trilha)
class TrilhaAdmin(SummernoteModelAdmin):
    list_display = ('id','titulo','linguagem')
    search_fields = ('id', 'titulo')
    ordering = ('id',)
    summernote_fields=('descricao')