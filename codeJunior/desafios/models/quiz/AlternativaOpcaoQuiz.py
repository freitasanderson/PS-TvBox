from django.db import models

from desafios.models import Trilha
from cadastro.models import Pessoa

class AlternativaOpcaoQuiz(models.Model):
  descricao = models.TextField(u'Descrição da opção do quiz', max_length=200)
  correta = models.BooleanField(verbose_name=u'Correta?',editable=True, default=True, help_text='Indica se a alternativa está correta')
  
  ativo = models.BooleanField(verbose_name=u'Está ativo?',editable=True, default=True, help_text='Indica se a alternativa está ativo')

  class Meta:
    verbose_name = 'Alternativa opção do quiz'
    verbose_name_plural = 'Alternativas das opções do quiz'

  def __str__(self):
      return f'{self.descricao}'
    
