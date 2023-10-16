from django.urls import path
from amanda.views import inicio, sugestoes
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sugestoes', sugestoes, name='sugestoes'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]