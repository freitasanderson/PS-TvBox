from django.db import models

from forum.models import Topico
from cadastro.models import Pessoa, Perfil
# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)

    topico = models.ForeignKey(Topico, verbose_name=("topico"), on_delete=models.CASCADE)
    
    quemPostou = models.ForeignKey(Perfil, verbose_name=('perfil'), on_delete=models.CASCADE)

    conteudo = models.TextField(u'Conteúdo do Post', max_length=2000)

    index = models.BooleanField(verbose_name=u'É o Primeiro Post?', default=False, editable=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'{self.id} {self.topico} {self.quemPostou}'
