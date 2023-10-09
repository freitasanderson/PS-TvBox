from django.contrib import admin

from forum.models import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','descricao','ativo')
    search_fields = ('id', 'nome')