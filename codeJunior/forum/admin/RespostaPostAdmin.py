from django.contrib import admin

from forum.models import RespostaPost

@admin.register(RespostaPost)
class RespostaPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post','resposta','ativo')
    search_fields = ('id',1)
    autocomplete_fields = ('post','resposta')