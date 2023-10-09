from django.db import models
from desafios.models import Linguagem

class Trilha(models.Model):
    titulo = models.TextField(verbose_name="Titulo da trilha", max_length=300)
    descricao = models.TextField(u'Descrição da Trilha', max_length=2000)
    desafios = models.ManyToManyField('Desafio', verbose_name="Desafios da trilha")  

    linguagem = models.ForeignKey(Linguagem, verbose_name='Linguagem da trilha', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Trilha de Conteúdo'
        verbose_name_plural = 'Trilhas de Conteúdos'

    
    def __str__(self):
        return self.titulo
