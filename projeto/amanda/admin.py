from django.contrib import admin

from django.db import models

# Modelo para a tabela Autor
class Autor(models.Model):
    Nome_do_Autor = models.CharField(max_length=255)  # Nome do autor

    def __str__(self):
        return self.Nome_do_Autor

# Modelo para a tabela Genero
class Genero(models.Model):
    Nome_do_Genero = models.CharField(max_length=255)  # Nome do gênero

    def __str__(self):
        return self.Nome_do_Genero

# Modelo para a tabela Editora
class Editora(models.Model):
    Nome_da_Editora = models.CharField(max_length=255)  # Nome da editora

    def __str__(self):
        return self.Nome_da_Editora

# Modelo para a tabela Livro
class Livro(models.Model):
    Título = models.CharField(max_length=255)  # Título do livro
    Ano_de_Publicacao = models.CharField(max_length=4)  # Ano de publicação
    Idioma = models.CharField(max_length=50)  # Idioma do livro
    Imagem = models.CharField(max_length=255)  # URL da imagem da capa
    Sinopse = models.TextField()  # Descrição do livro

    # Chaves estrangeiras para relacionar com as tabelas Autor, Genero e Editora
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Relaciona com a tabela Autor
    Genero = models.ForeignKey(Genero, on_delete=models.CASCADE)  # Relaciona com a tabela Genero
    Editora = models.ForeignKey(Editora, on_delete=models.CASCADE)  # Relaciona com a tabela Editora

    def __str__(self):
        return self.Título

