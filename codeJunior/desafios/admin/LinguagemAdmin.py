from django.contrib import admin

from desafios.models import Linguagem

@admin.register(Linguagem)
class LinguagemAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    search_fields = ('id','nome')