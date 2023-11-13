from django.contrib import admin

from desafios.models import Submissao

@admin.register(Submissao)
class SubmissaoAdmin(admin.ModelAdmin):
    list_display = ('id','problema','pessoa','dataSubmissao')
    search_fields = ('id', 'problema','pessoa','dataSubmissao')