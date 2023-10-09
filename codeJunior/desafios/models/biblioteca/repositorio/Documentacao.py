from django.db import models

from cadastro.models import Pessoa
from desafios.models import Linguagem

import uuid


class Documentacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome = models.CharField(u'Nome da Documentação', max_length=255)
    descricao = models.TextField(u'Descrição da Documentação', max_length=500, null=True, blank=True)

    tipo = models.ForeignKey(Linguagem, verbose_name='Tipo da Documentação', help_text="Guias, Manuais", on_delete=models.PROTECT,)

    arquivo = models.FileField(u'Arquivo', upload_to='biblioteca/repositorio/')
    
    quemCadastrou = models.ForeignKey(Pessoa, verbose_name='Quem Cadastrou', null=True, blank=True, default=None, on_delete=models.PROTECT)

    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = 'Documentação'
        verbose_name_plural = 'Documentações'
        ordering = ['dataCadastro','nome']

    def __str__(self):
        return f'{self.nome} - {self.tipo} ({self.dataCadastro})'
