# Generated by Django 4.0.1 on 2022-02-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0013_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, default='media\x0cotos\x018\x02\x822\\ProdutoPadrão.png', upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
