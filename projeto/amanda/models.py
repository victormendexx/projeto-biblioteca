#from django.contrib.auth.models import User
from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.CharField(max_length=4)
    idioma = models.CharField(max_length=50)
    imagem = models.CharField(max_length=100)
    sinopse = models.TextField()