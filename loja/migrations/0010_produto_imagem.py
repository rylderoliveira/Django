# Generated by Django 4.0.1 on 2022-02-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0009_alter_produto_fornecedor_alter_produto_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
