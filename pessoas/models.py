from django.db import models

# Create your models here.
class Pessoas(models.Model):
    usuario = models.CharField(max_length=225)
    senha = models.CharField(max_length=225)