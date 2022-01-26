from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista(request):
    return render(request, 'listaProdutos.html')

def cadastroProduto(request):
    return render(request, 'cadastroProduto.html')