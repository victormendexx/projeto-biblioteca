from django.urls import path
from amanda.views import inicio, avaliacoes, sobre, mostrar_livros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('avaliacoes', avaliacoes, name='avaliacoes'),
    path('sobre', sobre, name='sobre'),
    path('catalogo', mostrar_livros, name = 'catalogo'),
]
