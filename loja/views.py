from django.shortcuts import get_object_or_404, render, redirect

from loja.forms import ProductForm
from .models import Produto
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):

    produtos = Produto.objects.order_by('nome').filter(publicado=True)

    listaProdutos = {
        'lista': produtos
    }
    
    return render(request, 'loja/index.html', listaProdutos)

def lista(request):

    produtos = Produto.objects.order_by('nome').filter(cadastrado_por_id=request.user.id)

    listaProdutos = {
        'lista': produtos
    }
    
    return render(request, 'loja/listaProdutos.html', listaProdutos)

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
            return render(request, 'loja/editarProduto.html', context)


    context = {
        'form': form
    }
    return render(request, 'editarProduto.html', context)

def deletarProduto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect('lista')

def cadastroProduto(request):
    if request.method == "POST":
        user = get_object_or_404(User, pk=request.user.id)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            publicado = request.POST['publicado']
            
            if publicado == 'on':
                publicado = True
            else:
                publicado = False
            produto = Produto.objects.create(
                nome=request.POST['nome'], 
                fornecedor=request.POST['fornecedor'], 
                preco=request.POST['preco'], 
                cadastrado_por=user, 
                publicado=publicado, 
                imagem=request.FILES['imagem']
                )
            produto.save()
            messages.success(request, 'O produto %s foi cadastrado com sucesso' %request.POST['nome'])
            return redirect('lista')
        else:
            messages.error(request, 'Houve um erro na válidação dos dados')
            return render(request, 'loja/cadastroProduto.html', {'form': form})
    else:
        form = ProductForm
        return render(request, 'loja/cadastroProduto.html', {'form': form})