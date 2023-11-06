from django.contrib import admin

from desafios.models import RespostaQuiz
from django_summernote.admin import SummernoteModelAdmin

@admin.register(RespostaQuiz)

class RespostaQuizAdmin(SummernoteModelAdmin):
    list_display = ('id','quemRespondeu','opcao','alternativaSelecionada','quiz','dataCadastro',)
    search_fields = ('id', 'quemRespondeu')
    autocomplete_fields = ('opcao','alternativaSelecionada','quemRespondeu',)