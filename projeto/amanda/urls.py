from django.urls import path
from .views import index, sobre_nos

app_name = 'amanda'

urlpatterns = [
    path('', index, name='index'),
    path('sobre_nos', sobre_nos, name='sobre_nos'),
]