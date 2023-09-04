from django.db import models

class Problema(models.Model):
    DIFICULDADES = (
        ('basico', 'Básico'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    )

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    solucao = models.CharField(max_length=200)
    dificuldade = models.CharField(max_length=20, choices=DIFICULDADES)

    def __str__(self):
        return self.titulo
