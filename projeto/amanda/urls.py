from django.urls import path
from amanda.views import inicio

urlpatterns = [
    path('', inicio, name='inicio')
]