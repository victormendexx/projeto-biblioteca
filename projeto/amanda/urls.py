from django.urls import path
from amanda.views import inicio, sugestoes
from amanda.views import LoginViewClass, LogoutViewClass

urlpatterns = [
    path('login/', LoginViewClass.as_view(), name='login'),
    path('logout/', LogoutViewClass.as_view(), name='logout'),
    path('', inicio, name='inicio'),
    path('sugestoes', sugestoes, name='sugestoes'),
    ]