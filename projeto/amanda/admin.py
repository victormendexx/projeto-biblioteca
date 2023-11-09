from django.contrib import admin
from .models import Autor, Genero, Editora, Livro, Avaliacao

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('autor',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('genero',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('editora',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'editora', 'ano_publicacao', 'calcular_media_avaliacoes')
    list_filter = ('autor', 'genero', 'editora')
    search_fields = ('titulo', 'autor__autor', 'genero__genero', 'editora__editora')
    
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('user', 'livro', 'nota', 'comentario')
    list_filter = ('user', 'livro')
