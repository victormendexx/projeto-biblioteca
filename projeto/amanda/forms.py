from django import forms

class CatalogoFiltroForm(forms.Form):
    def __init__(self, *args, genero_choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genero'] = forms.ChoiceField(choices=genero_choices, required=False, initial='', widget=forms.Select(attrs={'class': 'seu-classe-css'}))