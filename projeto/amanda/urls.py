from django.urls import path
from amanda.views import inicio, sugestoes, mostrar_livros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sugestoes', sugestoes, name='sugestoes'),
    path('catalogo', mostrar_livros, name = 'catalogo'),
    ]