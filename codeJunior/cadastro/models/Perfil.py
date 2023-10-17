from django.db import models

from cadastro.models import Pessoa

class Perfil(models.Model):
    nome = models.CharField(verbose_name=u'Nome de Perfil',max_length=255)
    pessoa = models.OneToOneField(Pessoa, verbose_name=u'Pessoa', null=False, unique=True, on_delete=models.CASCADE)
    imagem = models.ImageField(u'Imagem de Perfil', upload_to="imagem/perfil", null=True, blank=True, help_text='Imagem que será mostrada em seu Perfil')

    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?',default=True, editable=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['nome','ativo']

    def __str__(self):
        return f'{self.nome}'
    

    def retornaPosts(self):
        quem = self
        totalPosts = quem.post_set.all().count()
        return totalPosts