from django.urls import path

from . import views
from loja.views import index

urlpatterns = [
    path('cadastroUsuario', views.cadastroUsuario, name='cadastroUsuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', index, name='dashboard'),

    
]