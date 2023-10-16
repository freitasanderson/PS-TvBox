from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from summernote.fields import SummernoteTextField


class TutorialDeInstalacao(models.Model):
    titulo = models.CharField(
        _("Título"),
        max_length=100,
        null=False,
        blank=False,
    )
    assunto = SummernoteTextField(
        _("Assunto/Descrição"),
        null=False,
        blank=False,
    )
    trilha = models.ForeignKey(
        "Trilha",
        verbose_name=_("Trilha"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    nivel = models.CharField(
        _("Nível"),
        max_length=10,
        choices=[
            ("iniciante", _("Iniciante")),
            ("intermediario", _("Intermediário")),
            ("avancado", _("Avançado")),
        ],
        null=False,
        blank=False,
    )
    quem_cadastrou = models.ForeignKey(
        User,
        verbose_name=_("Quem cadastrou"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    data_cadastro = models.DateTimeField(
        _("Data de cadastro"),
        auto_now_add=True,
    )
    data_alteracao = models.DateTimeField(
        _("Data de alteração"),
        auto_now=True,
    )
    ativo = models.BooleanField(
        _("Ativo"),
        default=True,
    )

    class Meta:
        verbose_name = _("Tutorial de instalação")
        verbose_name_plural = _("Tutoriais de instalação")

    def __str__(self):
        return self.titulo