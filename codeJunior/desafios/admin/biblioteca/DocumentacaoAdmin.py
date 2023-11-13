from django.contrib import admin

from desafios.models import Documentacao
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Documentacao)

class DocumentacaoAdmin(SummernoteModelAdmin):
    list_display = ('id','nome','tipo','quemCadastrou','dataCadastro','dataAlteracao','ativo')
    search_fields = ('id', 'nome','tipo','quemCadastrou')
    autocomplete_fields = ('tipo','quemCadastrou',)
    summernote_fields=('descricao')