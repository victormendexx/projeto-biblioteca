# Generated by Django 4.2.7 on 2023-11-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amanda', '0004_avaliacao_livro_delete_comment_avaliacao_livro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['nota'], 'verbose_name': 'Avaliacao', 'verbose_name_plural': 'Avaliacoes'},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'ordering': ['titulo'], 'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
        migrations.AlterField(
            model_name='livro',
            name='status',
            field=models.CharField(default='Disponível', max_length=30),
        ),
    ]