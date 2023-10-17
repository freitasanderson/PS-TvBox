from django.contrib import admin

from desafios.models import Desafio, Submissao, Trilha, Linguagem, Documentacao, OpcaoQuiz, Quiz, AlternativaOpcaoQuiz, RespostaQuiz, Emblema, Solucao


admin.site.register(Desafio)
admin.site.register(Solucao)
admin.site.register(Submissao)
admin.site.register(Trilha)
admin.site.register(Linguagem)
admin.site.register(Documentacao)
admin.site.register(Quiz)
admin.site.register(OpcaoQuiz)
admin.site.register(AlternativaOpcaoQuiz)
admin.site.register(RespostaQuiz)
admin.site.register(Emblema)