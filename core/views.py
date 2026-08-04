# Create your views here.
from django.shortcuts import render
from .models import Equipe

def index(request):
    # vai no banco de dados e pega todas as equipes cadastradas
    lista_equipes = Equipe.objects.all()

    # Prepara o "pacote" de dados que vai ser enviado para o template - HTML
    contexto = {
        'equipes': lista_equipes
    }

    # Redenriza a página e mistura o HTML com os dados do contexto
    return render(request, 'core/index.html', contexto)