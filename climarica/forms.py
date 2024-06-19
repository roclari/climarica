from django import forms
from .models import Noticia, Boletim, Contato


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'foto', 'resumo', 'conteudo', 'data_publicacao', 'autor']
        widgets = {
            'data_publicacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class BoletimForm(forms.ModelForm):
    class Meta:
        model = Boletim
        fields = ['titulo', 'conteudo', 'data_publicacao']
        widgets = {
            'data_publicacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'tel', 'assunto', 'data_publicacao']
        widgets = {
            'data_publicacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
