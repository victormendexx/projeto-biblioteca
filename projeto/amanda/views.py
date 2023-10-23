from django.shortcuts import render
from .forms import CommentForm
from django.contrib.auth.views import LoginView, LogoutView
from .dicio import dicionario_principal
# from .models import UserProfile 

class LoginViewClass(LoginView):
    """ 
        Login View Class """
    template_name = 'amanda/base_login.html'
    

class LogoutViewClass(LogoutView):
    """
        Simple Logout View Class"""
    next_page = '/'  # 'home' is the url name of your ho


def inicio(request):
    return render(request, 'amanda/inicio.html')

comments = []

def avaliacoes(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            comments.append({'name': name, 'text': text})
            form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'comments': comments,
        'form': form,
    }

    return render(request, 'amanda/avaliacoes.html', context)

def sobre(request):
    return render(request, 'amanda/sobre.html')

def catalogo(request):
    return render(request, 'amanda/catalogo.html', {'dicionario_principal': dicionario_principal})

def detalhes_livros(request, livro_id):
    chave = int(livro_id)
    livro = dicionario_principal.get(chave)
    descricao = "Descrição: Aqui você pode adicionar uma descrição sobre a história do livro."
    return render(request, 'amanda/detalhes_livros.html', {'livro': livro, 'descricao': descricao})