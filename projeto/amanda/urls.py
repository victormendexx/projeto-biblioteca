from django.urls import path
from amanda.views import inicio, avaliacoes, sobre, mostrar_livros
from amanda.views import LoginViewClass, LogoutViewClass

urlpatterns = [

    path('', inicio, name='inicio'),
    path('avaliacoes', avaliacoes, name='avaliacoes'),
    path('sobre', sobre, name='sobre'),
    path('catalogo', mostrar_livros, name = 'catalogo'),
    path('login/', LoginViewClass.as_view(), name='login'),
    path('logout/', LogoutViewClass.as_view(), name='logout'),
    #  path('profile/', views.user_profile, name='user_profile'),
    ]
