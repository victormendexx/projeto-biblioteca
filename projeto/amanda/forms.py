from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']

class FiltroCatalogoForm(forms.Form):
    genero = forms.CharField(required=False)
    ano_publicacao = forms.CharField(required=False)