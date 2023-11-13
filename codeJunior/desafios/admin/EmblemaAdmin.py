from django.contrib import admin

from desafios.models import Emblema

@admin.register(Emblema)
class EmblemaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','trilha')
    search_fields = ('id', 'nome')
    autocomplete_fields = ('trilha',)