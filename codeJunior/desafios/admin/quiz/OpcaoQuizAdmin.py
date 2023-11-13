from django.contrib import admin

from desafios.models import OpcaoQuiz
from django_summernote.admin import SummernoteModelAdmin

@admin.register(OpcaoQuiz)
class OpcaoQuizAdmin(SummernoteModelAdmin):
    list_display = ('id','titulo','ordem','ativo')
    search_fields = ('id','titulo')
    autocomplete_fields = ('alternativas',)
    summernote_fields = ('titulo')