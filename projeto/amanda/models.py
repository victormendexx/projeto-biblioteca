from django.db import models

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='livros/')
    sinopse = models.TextField()
    status = models.CharField(max_length=20, default="Disponível")
    pdf_disponivel = models.FileField(upload_to='pdfs/')
    def __str__(self):
        return self.titulo

class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"Avaliação de {self.livro.titulo} - Nota: {self.nota}"
