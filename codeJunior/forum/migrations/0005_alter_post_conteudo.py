# Generated by Django 4.2.4 on 2023-11-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0004_post_curtidas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="conteudo",
            field=models.TextField(max_length=500000, verbose_name="Conteúdo do Post"),
        ),
    ]