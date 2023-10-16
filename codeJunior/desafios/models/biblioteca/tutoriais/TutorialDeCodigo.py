from django.db import models
from django.utils import timezone
from summernote.fields import SummernoteField


class TutorialDeCodigo(models.Model):

    titulo = models.CharField(max_length=255, verbose_name="Título")
    assunto = SummernoteField(verbose_name="Assunto/Descrição")
    trilha = models.ForeignKey("Trilha", on_delete=models.CASCADE, related_name="tutoriales")
    nivel = models.CharField(
        max_length=255, choices=[("basico", "Básico"), ("intermediario", "Intermediário"), ("avancado", "Avançado")],
        verbose_name="Nível",
    )
    quem_cadastrou = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="tutoriales_cadastrados"
    )
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_alteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tutorial de código"
        verbose_name_plural = "Tutoriales de código"

    def __str__(self):
        return self.titulo