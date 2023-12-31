# Generated by Django 4.2.4 on 2023-11-06 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_curtidas'),
        ('desafios', '0012_tipotutorial_alter_linguagem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emblema',
            options={'ordering': ['id', 'trilha', 'nome'], 'verbose_name': 'Emblema', 'verbose_name_plural': 'Emblemas'},
        ),
        migrations.AddField(
            model_name='tutorial',
            name='topico',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.topico', verbose_name='Tópico no Fórum'),
        ),
    ]
