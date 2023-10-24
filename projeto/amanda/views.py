from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm
from django.contrib.auth.views import LoginView, LogoutView
from .dicio import dicionario_principal, status_emprestimo
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
    livro = dicionario_principal.get(livro_id)
    status = status_emprestimo.get(f"livro{livro_id}", {}).get('status', 'Indisponível')

    if not livro:
        return HttpResponse("Livro não encontrado")

    return render(request, 'amanda/detalhes_livros.html', {'livro': livro, 'status_emprestimo': status, 'livro_id': livro_id})