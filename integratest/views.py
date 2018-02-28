from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Data, Dados

def index(request):
    #output = "Teste Integração<br>"
    lista = Dados.objects.all()
    l = len(lista)
    output = "Testes de Integração<br><br>"
    for x in range(0, l):
        output += "<br> String de cadastro: "+str(lista[x].id_cli)+";"+str(lista[x].ponto)+";"+str(lista[x].nome_cli)
        output += "<br> Endereco: "+str(lista[x].endereco)+"<BR><BR>"

    return HttpResponse(output)