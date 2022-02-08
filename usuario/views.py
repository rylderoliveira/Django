from django.shortcuts import redirect, render

# Create your views here.
def cadastroUsuario(request):
    if request.method=="POST":
        usuario = request.POST['user']
        senha = request.POST['password']
        return redirect('login')
    else:
        return render(request, 'usuario/cadastroUsuario.html')

def login(request):
    return render(request, 'usuario/telaLogin.html')

def logout(request):
    pass

def dashboard(request):
    pass