from django.urls import path
from amanda.views import inicio, sugestoes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sugestoes', sugestoes, name='sugestoes'),
    ]