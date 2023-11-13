from django.contrib import admin

from desafios.models import Quiz
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Quiz)
class QuizAdmin(SummernoteModelAdmin):
    list_display = ('id','titulo','trilha','slug','quemCadastrou','ativo')
    search_fields = ('id', 'titulo','trilha','slug')
    ordering = ('id','dataCadastro','dataAlteracao','ativo')
    autocomplete_fields = ('opcoes',)
    summernote_fields=('descricao')