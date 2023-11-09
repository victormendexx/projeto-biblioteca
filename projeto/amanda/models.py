from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.autor  
      
    class Meta:
        ordering = ['autor']

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return self.genero
    
    class Meta:
        ordering = ['genero']

        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

class Editora(models.Model):
    id = models.AutoField(primary_key=True)
    editora = models.CharField(max_length=100)
    
    def __str__(self):
        return self.editora
    
    class Meta:
        ordering = ['editora']

        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='livros/')
    sinopse = models.TextField()
    status = models.CharField(max_length=30, default="Disponível")
    pdf_disponivel = models.FileField(upload_to='pdfs/')

    def calcular_media_avaliacoes(self):
        return Avaliacao.objects.filter(livro=self).aggregate(Avg('nota'))['nota__avg']
    
    def __str__(self):
        return f"{self.titulo} ({self.id})"

    class Meta:
        ordering = ['titulo']

        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)  # Adicione a propriedade "ID"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nota = models.FloatField(
        validators=[MaxValueValidator(limit_value=5.0)]
    )
    comentario = models.TextField()

    def __str__(self):
        return f"Avaliação de {self.livro.titulo} - Nota: {self.nota}"
    
    class Meta:
        ordering = ['nota']

        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'






