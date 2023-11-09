from django.contrib import admin
from .models import Livro, Autor, Genero, Editora, Avaliacao

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'editora', 'ano_publicacao', 'status')
    list_filter = ('status', 'genero', 'autor', 'editora')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('autor',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('genero',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('editora',)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('user', 'livro', 'nota', 'comentario')
    list_filter = ('livro',)
    search_fields = ('user__username', 'livro__titulo')
    
admin.site.register(Avaliacao, AvaliacaoAdmin)