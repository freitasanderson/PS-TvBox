from django.db import models

# Create your models here.
class Area(models.Model):
    id = models.BigAutoField(primary_key=True)

    nome = models.CharField(u'Nome da Área', max_length=255)
    descricao = models.TextField(u'Descrição da Área', max_length=500, null=True, blank=True)
    
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return self.nome
