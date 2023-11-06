from django.db import models

from forum.models import Secao, SubSecao
# Create your models here.
class Topico(models.Model):
    id = models.BigAutoField(primary_key=True)

    nome = models.CharField(u'Nome da Tópico', max_length=255)
    
    secao = models.ForeignKey(Secao, verbose_name=("secao"), on_delete=models.CASCADE)
    subsecao = models.ForeignKey(SubSecao, verbose_name=("subsecao"), null=True, blank=True, on_delete=models.CASCADE)
    
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Tópico"
        verbose_name_plural = "Tópicos"

    def __str__(self):
        return self.nome
