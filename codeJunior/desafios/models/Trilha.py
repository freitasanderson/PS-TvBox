from django.db import models
from desafios.models.Submissao import Submissao
from desafios.models.Linguagem import Linguagem
from desafios.models.Desafio import Desafio

# from desafios.models import Linguagem, Desafio

class Trilha(models.Model):
    titulo = models.TextField(verbose_name="Titulo da trilha", max_length=300)
    descricao = models.TextField(u'Descrição da Trilha', max_length=2000)
    desafios = models.ManyToManyField(Desafio, verbose_name="Desafios da trilha")  

    linguagem = models.ForeignKey(Linguagem, default=1,verbose_name='Linguagem da trilha', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Trilha de Conteúdo'
        verbose_name_plural = 'Trilhas de Conteúdos'

    
    def __str__(self):
        return self.titulo
    
    def checkCompletouTrilha(self):
        respostas = Submissao.objects.filter(problema__in=self.desafios.all(), resultado=1)

        if respostas.count() >= self.desafios.count():
            return True

        return False
