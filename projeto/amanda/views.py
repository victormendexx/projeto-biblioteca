from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm
from django.contrib.auth.views import LoginView, LogoutView
from .dicio import dicionario_principal, status_emprestimo
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import os
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


def pegar_emprestado(request, livro_id):
    status_info = status_emprestimo.get(livro_id)
    
    if status_info and status_info["status"] == "Disponível":
        pdf_path = status_info.get("pdf_disponivel", "")
        
        if pdf_path:
            with open(pdf_path, 'rb') as pdf_file:
                response = FileResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_path)}'
                status_info['status'] = "Indisponível"
                return response
    return HttpResponse("Livro não encontrado ou indisponível")

def devolver_emprestado(request, livro_id):
    if request.method == 'POST':
        uploaded_file = request.FILES['pdf_upload']
        status_info = status_emprestimo.get(livro_id)

        if status_info['status'] and uploaded_file.name == os.path.basename(status_info.get("pdf_disponivel", "")):
            status_info['status'] = "Disponível"
            return HttpResponse("Livro devolvido com sucesso")
    
    return HttpResponseRedirect(reverse('detalhes_livros', kwargs={'livro_id': livro_id}))