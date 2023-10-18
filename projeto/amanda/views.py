from django.shortcuts import render
from .forms import CommentForm, FiltroCatalogoForm
from django.contrib.auth.views import LoginView, LogoutView
from .dicio import dicionario_principal

from django.shortcuts import render
from .forms import FiltroCatalogoForm  # Import your form from the appropriate module

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

def mostrar_livros(request):
    return render(request, 'amanda/catalago.html', {'livros': dicionario_principal})


def catalogo(request):
    livros_filtrados = None

    if request.method == "POST":
        filtro_form = FiltroCatalogoForm(request.POST)
        if filtro_form.is_valid():
            genero = filtro_form.cleaned_data.get('genero')
            ano_publicacao = filtro_form.cleaned_data.get('ano_publicacao')

            # Create a base query
            #ivros_query = Livro.objects.all()

            # if genero:
            #     livros_query = livros_query.filter(genero=genero)

            # if ano_publicacao:
            #     livros_query = livros_query.filter(ano_publicacao=ano_publicacao)

            # Execute the query and get the filtered books
            #livros_filtrados = livros_query

    else:
        filtro_form = FiltroCatalogoForm()

    context = {
        'filtro_form': filtro_form,
        'livros': livros_filtrados
    }

    return render(request, 'amanda/catalogo.html', context)
