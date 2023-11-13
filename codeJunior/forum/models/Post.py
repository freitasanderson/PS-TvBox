from collections.abc import Iterable
from django.db import models
from django.apps import apps

from forum.models import Topico
from cadastro.models import Pessoa, Perfil
from desafios.models import TipoTutorial
# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)

    topico = models.ForeignKey(Topico, verbose_name=("topico"), on_delete=models.CASCADE)
    
    quemPostou = models.ForeignKey(Perfil, verbose_name=('perfil'), on_delete=models.CASCADE)

    conteudo = models.TextField(u'Conteúdo do Post', max_length=500000)

    index = models.BooleanField(verbose_name=u'É o Primeiro Post?', default=False, editable=True)
    
    curtidas = models.IntegerField(u'Curtidas', default=0)
    
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'{self.id} {self.topico} {self.quemPostou}'

    def save(self):        
        secao = self.topico.secao

        if secao.area.nome == 'Tutoriais' and self.index:

            Tutorial = apps.get_model('desafios.Tutorial')

            novo_item = Tutorial()
            novo_item.titulo = self.topico.nome
            novo_item.assunto = self.conteudo
            novo_item.tipo = TipoTutorial.objects.get(titulo=secao)
            novo_item.nivel = 1
            novo_item.quemCadastrou = self.quemPostou

        return super().save()