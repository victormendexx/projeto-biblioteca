from django.contrib import admin
from .models import Livro, Avaliacao

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'editora', 'ano_publicacao', 'status')
    search_fields = ('titulo', 'autor', 'genero', 'editora')
    list_filter = ('status', 'genero')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'nota', 'comentario')
    list_filter = ('nota',)