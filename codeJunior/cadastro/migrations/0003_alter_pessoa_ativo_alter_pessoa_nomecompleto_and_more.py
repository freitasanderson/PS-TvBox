# Generated by Django 4.2.1 on 2023-05-07 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastro', '0002_alter_pessoa_options_pessoa_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nomeCompleto',
            field=models.CharField(max_length=255, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]