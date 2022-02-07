from django.contrib import admin
from .models import Produto

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'fornecedor', 'preco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'fornecedor')
    list_filter = ('fornecedor',)
    list_per_page = 10

# Register your models here.
admin.site.register(Produto, ListandoProdutos)