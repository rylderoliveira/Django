from django.db import models
from pessoas.models import Pessoas

# Create your models here.
class Produto(models.Model):
    cadastrado_por = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    fornecedor = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    publicado = models.BooleanField(default=False)