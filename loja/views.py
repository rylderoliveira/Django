from django.shortcuts import get_object_or_404, render
from .models import Produto

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista(request):

    produtos = Produto.objects.all()

    listaProdutos = {
        'lista': produtos
    }
    
    return render(request, 'listaProdutos.html', listaProdutos)

def cadastroProduto(request):
    return render(request, 'cadastroProduto.html')

def editarProduto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto_a_ixibir = {
        'produto': produto
    }
    return render(request, 'editarProduto.html', produto_a_ixibir)