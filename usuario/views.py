from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from loja.models import Produto
from loja.forms import ProductForm
from django.contrib import messages

# Create your views here.
def cadastroUsuario(request):
    if request.method=="POST":
        usuario = request.POST['user']
        senha = request.POST['password']

        # Validações
        if not usuario.strip():
            messages.error(request, 'Usuario inválido')
            print('Usuario Invalido')
            return redirect('cadastroUsuario')
        
        if not senha.strip():
            messages.error(request, 'Senha inválida')
            return redirect('cadastroUsuario')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuario já cadastrado')
            return redirect('cadastroUsuario')
        
        user = User.objects.create_user(username=usuario, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuario/cadastroUsuario.html')

def login(request):
    if request.method=="POST":
        usuario = request.POST['user']
        senha = request.POST['password']

        #Validações
        if not usuario.strip() or not senha.strip():
            messages.error(request, 'Usuario ou senha inválidos')
            return redirect('login')

        if User.objects.filter(username=usuario).exists():
            user = auth.authenticate(request, username=usuario, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'usuario/telaLogin.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'usuario/dashboard.html')
    else:
        return redirect('index')

def cadastroProduto(request):
    if request.method == "POST":
        user = get_object_or_404(User, pk=request.user.id)
        form = ProductForm(request.POST)
        if form.is_valid():
            publicado = request.POST['publicado']
            if publicado == 'on':
                publicado = True
            else:
                publicado = False
            produto = Produto.objects.create(nome=request.POST['nome'], fornecedor=request.POST['fornecedor'], preco=request.POST['preco'], cadastrado_por=user, publicado=publicado)
            produto.save()
            messages.success(request, 'O produto %s foi cadastrado com sucesso' %request.POST['nome'])
            return redirect('lista')
        else:
            messages.error(request, 'Houve um erro na válidação dos dados')
            return render(request, 'cadastroProduto.html', {'form': form})
    else:
        form = ProductForm
        return render(request, 'cadastroProduto.html', {'form': form})





    # if request.method=="POST":
    #     nome = request.POST['produto']
    #     fornecedor = request.POST['fornecedor']
    #     preco = request.POST['preco']
    #     cadastrado_por = get_object_or_404(User, pk=request.user.id)
    #     publicado = request.POST['publicado']

    #     if publicado == 'on':
    #         publicado = True
    #     else:
    #         publicado = False

    #     # Validações
    #     if not nome.strip():
    #         print('Nome invalido')
    #         return redirect('cadastroProduto')
        
    #     if not fornecedor.strip():
    #         print('Fornecedor invalido')
    #         return redirect('cadastroProduto')
        
    #     if preco is None:
    #         print('Preço invalido')
    #         return redirect('cadastroProduto')

    #     if Produto.objects.filter(nome=nome).exists():
    #         print('Produto já cadastrado')
    #         return redirect('cadastroProduto')
        
    #     produto = Produto.objects.create(nome=nome, fornecedor=fornecedor, preco=preco, cadastrado_por=cadastrado_por, publicado=publicado)
    #     produto.save()
    #     print(publicado)
    #     print('Produto cadastrado com sucesso')
    #     return redirect('lista')
    # else:
    #     return render(request, 'cadastroProduto.html')

