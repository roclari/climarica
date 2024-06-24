from django.db import models
from django.utils import timezone


class Noticia(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    foto = models.FileField(upload_to='media/', null=True, blank=True)
    resumo = models.TextField(null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)
    data_publicacao = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=100, default='Autor', null=True, blank=True)

    def __str__(self):
        return self.titulo


class Boletim(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    fonte = models.CharField(max_length=100, default='https://www.marica.rj.gov.br/previsao-do-tempo/', null=True, blank=True)

    def __str__(self):
        return self.titulo


class Contato(models.Model):
    ASSUNTOS = [('sugestao', 'Quero fazer uma sugestão'),
                ('elogio', 'Quero fazer um elogio'), ]

    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    tel = models.CharField(max_length=15, null=True, blank=True)
    assunto = models.CharField(max_length=50, choices=ASSUNTOS, default='---', null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assunto
