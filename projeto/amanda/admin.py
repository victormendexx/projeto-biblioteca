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
    list_display = ('titulo', 'nota_media_display')
    readonly_fields = ('nota_media_display',)

    def nota_media_display(self, obj):
        return obj.nota_media
    nota_media_display.short_description = 'Nota Média'
    
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('user', 'livro', 'nota', 'comentario')
    list_filter = ('user', 'livro')
