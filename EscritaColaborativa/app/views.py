"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import *
from datetime import datetime
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.db import connection
import json

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def editar_historia(request):
    historias = Historia.objects.all()
    return render(
        request,
        'app/editar_historia.html',
        context_instance = RequestContext(request,
        {
            'historias': historias,            
        })
    )

def listar_historia(request):
    historias = Historia.objects.all()
    return render(
        request,
        'app/historia.html',
        context_instance = RequestContext(request,
        {
            'historias': historias,            
        })
    )

def listar_interacao_historia(request):
    if request.GET['cod_hist']:
        primeiro_paragrafo = Historia.objects.get(cod_hist = request.GET['cod_hist'])
        interacoes = Partes.objects.filter(cod_hist_id = primeiro_paragrafo.id)
        data_array = []

        for item in interacoes:        

            dados = {   "titulo" :primeiro_paragrafo.tit_hist,
                        "primeiro_paragrafo" : primeiro_paragrafo.prim_parag, 
                        "interacao" : item.desc_parte,
                        "escritor" : item.cod_escrit_id
                    }

            data_array.append(dados)

        return HttpResponse(json.dumps(data_array))


    
       

def validar_escritor(request):

    historia = request.GET['cod_hist']
    escritor = request.GET['cod_escr']
    acesso = 'negado'
    mensagem = ''

    data_atual = datetime.now

    #   Verifica Interação do dia
    
    sequencia_escritor = Participantes.objects.get(cod_escrit = escritor).seq_particip
    escritor = Escritores.objects.get(cod_escrit = escritor)

    if Partes.objects.filter(data_inicio = data_atual, cod_escrit_id = escritor.id):
        acesso = 'negado'
        mensagem = 'Interação já realizada hoje'
    else:

        if int(sequencia_escritor)-1 != 0:
            if Partes.objects.filter(data_inicio = data_atual, cod_escrit_id = Partes.objects.filter(data_inicio = data_atual, cod_escrit_id = escritor.id -1)):
                
                if Participantes.objects.filter(cod_hist = historia , cod_escrit = escritor):
                    acesso ='liberado'
                else:
                    acesso = 'negado'    

            else:
                acesso = 'negado'

        else:

            if Participantes.objects.filter(cod_hist = historia , cod_escrit = escritor):
                acesso ='liberado'
            else:
                acesso = 'negado'

        
    return HttpResponse(acesso)


def salvar_edicao(request):
    

    if request.POST['descricao_historia'] != "":
        escritor= Escritores.objects.get(cod_escrit = request.POST['cod_escr'])
        historia = Historia.objects.get(cod_hist = request.POST['cod_hist'])
    
        parte = Partes()
        parte.cod_escrit = escritor
        parte.cod_hist = historia
        parte.desc_parte = request.POST['descricao_historia']
    
        parte.save()
        return render(
            request,
            'app/editar_historia.html',
            context_instance = RequestContext(request,
            {
                'historias': Historia.objects.all(),            
                'mensage': 'Salvo com sucesso',
                'tipo': 'sucesso'
            })
        )
    else:
        return render(
            request,
            'app/editar_historia.html',
            context_instance = RequestContext(request,
            {
                'historias': Historia.objects.all(),            
                'mensage': 'Favor Preencher a descrição',
                'tipo': 'erro'
            })
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
