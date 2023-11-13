from django.db import models

from cadastro.models import Pessoa
from desafios.models import Trilha

class TipoTutorial(models.Model):
    id = models.BigAutoField(primary_key=True)

    titulo = models.CharField(u"Título", max_length=255)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Tipo de Tutorial"
        verbose_name_plural = "Tipos de Tutoriais"

    def __str__(self):
        return self.titulo