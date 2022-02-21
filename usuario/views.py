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

