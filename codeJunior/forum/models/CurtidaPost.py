from django.db import models

from forum.models import Post
from cadastro.models import Perfil

class CurtidaPost(models.Model):
    id = models.BigAutoField(primary_key=True)

    post = models.ForeignKey(Post, verbose_name=u'Post', on_delete=models.CASCADE)

    quemCurtiu = models.ForeignKey(Perfil, verbose_name='Perfil', on_delete=models.CASCADE)
    
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Curtida Post"
        verbose_name_plural = "Curtidas Posts"

    def __str__(self):
        return self.quemCurtiu