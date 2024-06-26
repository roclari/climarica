from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *


def index(request):
    noticias = Noticia.objects.all()
    return render(request, 'index.html', {'noticias': noticias})


def about(request):
    return render(request, 'about.html')


def contact(request):
    assuntos = Contato.ASSUNTOS
    return render(request, 'contact.html', {'assuntos': assuntos})


def news(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    noticias_destaque = noticias[:3]
    outras_noticias = noticias[3:]

    context = {
        'noticias_destaque': noticias_destaque,
        'outras_noticias': outras_noticias
    }
    return render(request, 'news.html', context)


def news_details(request, news_id):
    noticia = get_object_or_404(Noticia, pk=news_id)
    return render(request, 'news_details.html', {'noticia': noticia})


def reports(request):
    boletins = Boletim.objects.all()
    selected_boletim = None

    if request.method == 'POST':
        boletim_id = request.POST.get('boletim')
        if boletim_id:
            selected_boletim = get_object_or_404(Boletim, pk=boletim_id)

    return render(request, 'reports.html', {'boletins': boletins,
                                            'selected_boletim': selected_boletim})


def weather(request):
    return render(request, 'weather.html')
