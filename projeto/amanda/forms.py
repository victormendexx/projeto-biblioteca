from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']


class CatalogoFiltroForm(forms.Form):
    genero = forms.CharField(required=False)


