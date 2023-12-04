from django.db import models

from forum.models import Post

class RespostaPost(models.Model):
    id = models.BigAutoField(primary_key=True)

    post = models.ForeignKey(Post, verbose_name=u'Post', related_name='post', on_delete=models.CASCADE)
    resposta = models.ForeignKey(Post, verbose_name=u'Resposta', related_name='resposta', on_delete=models.CASCADE)
    
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Resposta Post"
        verbose_name_plural = "Respostas Posts"

    def __str__(self):
        return f'{self.id}'
