from django.urls import path
from amanda.views import inicio, avaliacoes, sobre

urlpatterns = [
    path('', inicio, name='inicio'),
    path('avaliacoes', avaliacoes, name='avaliacoes'),
    path('sobre', sobre, name='sobre'),
]