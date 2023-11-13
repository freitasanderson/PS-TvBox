from django.db import models

CHOICE_DIFICULDADES = (
    (1, 'Básico'),
    (2, 'Intermediário'),
    (3, 'Avançado'),
)

class Desafio(models.Model):
    titulo = models.CharField(u'Título do Desafio', max_length=200)
    descricao = models.TextField(u'Descrição do Desafio')
    dificuldade = models.IntegerField(u'Nível do Desafio', choices=CHOICE_DIFICULDADES, default=1)
    estimativa = models.DecimalField(u'Estimativa de tempo em minutos', default=5, decimal_places=2, max_digits=10)
    ordem = models.IntegerField(u'Ordenação', default=5,)

    ativo = models.BooleanField(verbose_name=u'Está ativo?',editable=True, default=True, help_text='Indica se o desafio está ativo')

    class Meta:
        ordering = ['ordem',]

    def __str__(self):
        return f'{self.id} - {self.titulo}'
    
