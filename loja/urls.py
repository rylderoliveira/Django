from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listaProdutos', views.lista, name='lista'),
    path('editar/<int:produto_id>', views.editarProduto, name='editarProduto'),
    path('deletar/<int:produto_id>', views.deletarProduto, name='deletarProduto'),
]