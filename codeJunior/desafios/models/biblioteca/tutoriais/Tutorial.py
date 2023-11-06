from django.db import models

from cadastro.models import Pessoa
from desafios.models import Trilha, TipoTutorial
from forum.models import Topico
NIVEL_CHOICES = [
    ("0", "Básico"), 
    ("1", "Intermediário"), 
    ("2", "Avançado")
]

class Tutorial(models.Model):
    id = models.BigAutoField(primary_key=True)

    titulo = models.CharField(u"Título", max_length=255)
    assunto = models.TextField(u"Assunto/Descrição", max_length=50000)
    trilha = models.ForeignKey(Trilha, verbose_name="Trilha", on_delete=models.CASCADE)

    topico = models.ForeignKey(Topico, verbose_name="Tópico no Fórum", null=True, blank=True, default=None, on_delete=models.CASCADE)
    
    tipo = models.ForeignKey(TipoTutorial, verbose_name="Tipo", related_name='tutoriais',on_delete=models.CASCADE)
    nivel = models.CharField(u"Nível", choices=NIVEL_CHOICES)

    quemCadastrou = models.ForeignKey(Pessoa, verbose_name='Quem Cadastrou', null=True, blank=True, default=None, on_delete=models.PROTECT)

    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutoriais"

    def __str__(self):
        return self.titulo