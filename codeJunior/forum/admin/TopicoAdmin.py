from django.contrib import admin

from forum.models import Topico

@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','secao','subsecao','ativo')
    search_fields = ('id', 'nome', 'secao','subsecao')
    autocomplete_fields = ('secao','subsecao')