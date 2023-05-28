from django.shortcuts import render
from django.http import HttpResponse
from locadora.models import Filme, Locacao
# Create your views here.

def index(request):
    context = {'aluno' : 'Bruno Pereira de  Souza'}
    return render(request, "index.html", context)

def lista_locacao(request):
    locacoes = Locacao.objects.all()
    context = {'locacoes' : locacoes}
    return render(request, "lista_locacoes.html", context)

def lista_filmes(request):
    filmes = Filme.objects.all()
    context = {'filmes' : filmes}
    return render(request, "lista_filmes.html", context)