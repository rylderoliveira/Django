from django.shortcuts import get_object_or_404, render, redirect

from loja.forms import ProductForm
from .models import Produto
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista(request):

    produtos = Produto.objects.order_by('nome').filter(publicado=True)

    listaProdutos = {
        'lista': produtos
    }
    
    return render(request, 'listaProdutos.html', listaProdutos)

def editarProduto(request, produto_id):
        
    produto = get_object_or_404(Produto, pk=produto_id)
    form = ProductForm(instance=produto)

    if request.method=='POST':
        form = ProductForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'O produto %s foi editado com sucesso' %request.POST['nome'])
            return redirect('lista')
        else:
            messages.error(request, 'Houve um erro na validação dos dados')
            return render(request, 'editarProduto.html', context)


    context = {
        'form': form
    }
    return render(request, 'editarProduto.html', context)

def deletarProduto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect('lista')
    