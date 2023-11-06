from django.contrib import admin

from desafios.models import Solucao

@admin.register(Solucao)
class SolucaoAdmin(admin.ModelAdmin):
    list_display = ('id','desafio','entrada','secreta','ativo')
    search_fields = ('id', 'desafio')
    autocomplete_fields = ('desafio',)