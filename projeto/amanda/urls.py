from django.urls import path
from amanda.views import inicio, sobre, catalogo, detalhes_livros
from amanda.views import LoginViewClass, LogoutViewClass
from . import views

urlpatterns = [

    path('', inicio, name='inicio'),
    path('sobre/', sobre, name='sobre'),
    path('catalogo/', catalogo, name = 'catalogo'),
    path('login/', LoginViewClass.as_view(), name='login'),
    path('logout/', LogoutViewClass.as_view(), name='logout'),
    path('livro<int:livro_id>/', detalhes_livros, name='detalhes_livros'),
    path('search/', views.search_view, name='search_view'),
    ]