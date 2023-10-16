from django.shortcuts import render
from .forms import CommentForm
from .dicio import dicionario_principal

def inicio(request):
    return render(request, 'amanda/inicio.html')

comments = []

def sugestoes(request):
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

    return render(request, 'amanda/sugestoes.html', context)

def mostrar_livros(request):
    return render(request, 'amanda/catalago.html', {'livros': dicionario_principal})
