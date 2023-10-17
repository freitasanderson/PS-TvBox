from django.db import models

from desafios.models.Trilha import Trilha

class Emblema(models.Model):
    nome = models.CharField(u'Nome do Emblema', max_length=200)
    descricao = models.TextField(u'Descrição do Emblema')
    imagem = models.ImageField(u'Imagem do Emblema', upload_to='emblemas/')
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome