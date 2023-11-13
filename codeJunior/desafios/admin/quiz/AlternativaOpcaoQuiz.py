from django.contrib import admin

from desafios.models import AlternativaOpcaoQuiz

@admin.register(AlternativaOpcaoQuiz)
class AlternativaOpcaoQuizAdmin(admin.ModelAdmin):
    list_display = ('id','descricao','correta','ativo')
    search_fields = ('id','descricao')