from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    fornecedor = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2)