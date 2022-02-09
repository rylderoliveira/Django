from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastroUsuario(request):
    if request.method=="POST":
        usuario = request.POST['user']
        senha = request.POST['password']

        # Validações
        if not usuario.strip():
            print('Usuario Invalido')
            return redirect('cadastroUsuario')
        
        if not senha.strip():
            print('Senha Invalida')
            return redirect('cadastroUsuario')

        if User.objects.filter(username=usuario).exists():
            print('Usuario já cadastrado')
            return redirect('cadastroUsuario')
        
        user = User.objects.create_user(username=usuario, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuario/cadastroUsuario.html')

def login(request):
    if request.method=="POST":
        usuario = request.POST['user']
        senha = request.POST['password']

        #Validações
        if usuario == '' or senha == '':
            print('Usuario ou senha invalidos')
            return redirect('login')

        if User.objects.filter(username=usuario).exists():
            user = auth.authenticate(request, username=usuario, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
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