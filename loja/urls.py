from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listaProdutos', views.lista, name='lista'),
    path('cadastroProdutos', views.cadastroProduto, name='cadastroProduto'),
    path('<int:produto_id>', views.editarProduto, name='editarProduto'),
]