from django.shortcuts import render
from .forms import CommentForm
from django.contrib.auth.views import LoginView, LogoutView
from .dicio import dicionario_principal, filtrar_por_genero, obter_lista_generos
from .forms import CatalogoFiltroForm
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
    choices_generos = obter_lista_generos(dicionario_principal)

    if request.method == "POST":        
        form = CatalogoFiltroForm(request.POST,genero_choices=choices_generos)   

    if form.is_valid():
        genero = form.cleaned_data.get('genero')
        if genero:
            livros_filtrados = filtrar_por_genero(dicionario_principal, genero)
        else:
            livros_filtrados=dicionario_principal


        context = {
            'dicionario_principal': livros_filtrados,
            'form': form,
        }
    else:
        form = CatalogoFiltroForm(genero_choices=choices_generos)
        context = {
            'dicionario_principal': dicionario_principal,
            'form': form,
        }
    return render(request, 'amanda/catalogo.html', context)

def detalhes_livros(request, livro_id):
    chave = int(livro_id)
    livro = dicionario_principal.get(chave)
    descricao = "Descrição: Aqui você pode adicionar uma descrição sobre a história do livro."
    return render(request, 'amanda/detalhes_livros.html', {'livro': livro, 'descricao': descricao})

def search_view(request):
    query = request.GET.get('q', '')  # Obtenha os termos de pesquisa da URL
    results = []

    # Itere sobre o dicionário de dados e encontre resultados correspondentes
    for livro_id, livro_info in dicionario_principal.items():
        if query.lower() in livro_info['titulo'].lower():
            results.append(livro_info)

    context = {
        'results': results,
        'query': query,
    }

    return render(request, 'amanda/search_results.html', context)

