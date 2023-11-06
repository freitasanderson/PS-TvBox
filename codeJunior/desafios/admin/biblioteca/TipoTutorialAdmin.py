from django.contrib import admin

from desafios.models import TipoTutorial

@admin.register(TipoTutorial)
class TipoTutorialAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','ativo')
    search_fields = ('id','titulo')