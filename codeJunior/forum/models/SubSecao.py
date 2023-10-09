from django.db import models

from forum.models import Secao
# Create your models here.
class SubSecao(models.Model):
    id = models.BigAutoField(primary_key=True)

    nome = models.CharField(u'Nome da Subseção', max_length=255)
    descricao = models.TextField(u'Descrição da Subseção', max_length=500, null=True, blank=True)
    
    secao = models.models.ForeignKey(Secao, verbose_name=("secao"), on_delete=models.CASCADE)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Subseção"
        verbose_name_plural = "Subseções"

    def __str__(self):
        return self.nome
