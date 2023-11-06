from django.contrib import admin

from desafios.models import Tutorial
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Tutorial)
class TutorialAdmin(SummernoteModelAdmin):
    list_display = ('id','titulo','tipo','trilha','nivel','quemCadastrou','ativo')
    search_fields = ('id','titulo','tipo','trilha')
    summernote_fields=('assunto')
    autocomplete_fields=('topico',)