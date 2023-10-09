from django.db import models

from forum.models import Area
# Create your models here.
class Secao(models.Model):
    id = models.BigAutoField(primary_key=True)

    nome = models.CharField(u'Nome da Seção', max_length=255)
    descricao = models.TextField(u'Descrição da Seção', max_length=500, null=True, blank=True)
    
    area = models.ForeignKey(Area, verbose_name=("Area"), on_delete=models.CASCADE)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Seção"
        verbose_name_plural = "Seções"

    def __str__(self):
        return self.nome
