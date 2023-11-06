from django.db import models

from desafios.models import Trilha, OpcaoQuiz
from cadastro.models import Pessoa

class Quiz(models.Model):
  titulo = models.TextField(verbose_name="Titulo do quiz", max_length=300)
  descricao = models.TextField(u'Descrição do quiz', max_length=20000)
  trilha = models.ForeignKey(Trilha, verbose_name='Trilha do quiz', on_delete=models.PROTECT, null=True)
  slug = models.SlugField('Slug', max_length=150, unique=True, blank=False, null=False)
  quemCadastrou = models.ForeignKey(Pessoa, verbose_name='Quem cadastrou', on_delete=models.PROTECT)

  dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True)
  dataAlteracao = models.DateTimeField(u'Data de Alteração', auto_now=True)

  opcoes = models.ManyToManyField(OpcaoQuiz, verbose_name='Opções do Quiz', blank=False)

  ativo = models.BooleanField(verbose_name=u'Está ativo?',editable=True, default=True, help_text='Indica se o quiz está ativo')

  class Meta:
    verbose_name = 'Quiz'
    verbose_name_plural = 'Quiz'

  def __str__(self):
      return f'{self.titulo}'
    
