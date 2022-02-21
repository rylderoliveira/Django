from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
    cadastrado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    fornecedor = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    publicado = models.BooleanField(default=False)
    imagem = models.ImageField(default='ProdutoPadrão', blank=True, upload_to='fotos/%d/%m/%Y/', null=True)