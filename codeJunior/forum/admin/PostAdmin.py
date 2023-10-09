from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from forum.models import Post

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)
    list_display = ('id', 'topico','quemPostou','index','ativo')
    search_fields = ('id', 'topico', 'quemPostou')
    autocomplete_fields = ('topico','quemPostou')
