from pdb import post_mortem
from tkinter import Widget
from django.forms import ModelForm
from .models import Produto

class ProductForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','fornecedor','preco','publicado', 'imagem']
        