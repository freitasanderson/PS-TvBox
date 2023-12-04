from django.db import models

class Emblema(models.Model):
    nome = models.CharField(u'Nome do Emblema', max_length=200)
    descricao = models.TextField(u'Descrição do Emblema')
    imagem = models.ImageField(u'Imagem do Emblema', upload_to='emblemas/')
    trilha = models.ForeignKey('Trilha', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Emblema'
        verbose_name_plural = 'Emblemas'
        ordering = ['id','trilha','nome']

    def __str__(self):
        return self.nome