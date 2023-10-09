from django.contrib import admin

from forum.models import Secao

@admin.register(Secao)
class SecaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','descricao','area','ativo')
    search_fields = ('id', 'nome', 'area')
    autocomplete_fields = ('area',)