from django.contrib import admin
from .models import Pessoas

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'usuario')
    list_display_links = ('id', 'usuario')
    search_fields = ('usuario',)
    list_per_page = 10

# Register your models here.
admin.site.register(Pessoas, ListandoPessoas)