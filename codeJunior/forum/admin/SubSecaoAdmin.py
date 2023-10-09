from django.contrib import admin

from forum.models import SubSecao

@admin.register(SubSecao)
class SubSecaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','descricao','secao','ativo')
    search_fields = ('id', 'nome', 'secao')
    autocomplete_fields = ('secao',)