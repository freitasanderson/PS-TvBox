from django.db import models

class Solucao(models.Model):
  desafio = models.ForeignKey('Desafio', verbose_name='Desafio', on_delete=models.PROTECT, null=False)

  entrada = models.CharField(verbose_name=u'Entrada', max_length=200)
  secreta = models.BooleanField(verbose_name=u'Secreta?',editable=True, default=True, help_text='Indica se o solucao é secreta')
  saida = models.CharField(verbose_name=u'Saida', max_length=200)
  
  ativo = models.BooleanField(verbose_name=u'Está ativo?',editable=True, default=True, help_text='Indica se o solucao está ativo')

  class Meta:
    verbose_name = 'Solução do desafio'
    verbose_name_plural = 'Soluções dos desafios'

  def __str__(self):
      return f'Solução {self.id} - {self.desafio}'
    
