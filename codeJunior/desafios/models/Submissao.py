from django.db import models

from cadastro.models import Pessoa

CHOICES_RESULTADO_SUBMISSAO = (
    (1, 'Correta'),
    (2, 'Incorreta'),
)

class Submissao(models.Model):
    problema = models.ForeignKey('Desafio', on_delete=models.CASCADE, related_name='submissao')
    codigo = models.TextField()
    resultado = models.IntegerField(u'Resultado', default=1, choices=CHOICES_RESULTADO_SUBMISSAO)

    pessoa = models.ForeignKey(Pessoa, verbose_name=u'Pessoa', null=False, on_delete=models.CASCADE)
    dataSubmissao = models.DateTimeField('Data de Submissão', auto_now_add=True, null=True)
    class Meta:
        verbose_name = 'Submissão'
        verbose_name_plural = 'Submissões'
        ordering = ['problema__id','id']

    def __str__(self):
        return f'{self.id} - {self.codigo}'
