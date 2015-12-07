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
    escritores = Escritores.objects.all()
    return render(
        request,
        'app/editar_historia.html',
        context_instance = RequestContext(request,
        {
            'historias': historias,
            'escritores': escritores,
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
    
    cod_historia = request.GET.get('cod_hist', '')
    cod_escritor = request.GET.get('cod_escrit', '')

    #   Verifica Interação do dia
    
    print('cod:' + cod_historia)

    if not cod_historia or cod_historia == '0':
        dados = {   "acesso" : 'negado',
                    "message" : 'Selecione uma história válida.'
                }
        return HttpResponse(json.dumps(dados))



    if not cod_escritor or cod_escritor == '0':
        dados = {   "acesso" : 'negado',
                    "message" : 'Selecione um escritor válido.'
                }
        return HttpResponse(json.dumps(dados))



    if Historia.objects.filter(cod_hist = cod_historia):
        historia = Historia.objects.filter(cod_hist = cod_historia)
    else:
        dados = {   "acesso" : 'negado',
                    "message" : 'Selecione uma história válida.'
                }
        return HttpResponse(json.dumps(dados))



    if Escritores.objects.filter(cod_escrit = cod_escritor):
        escritor = Escritores.objects.get(cod_escrit = cod_escritor)
    else:
        dados = {   "acesso" : 'negado',
                    "message" : 'Selecione um escritor válido.'
                }
        return HttpResponse(json.dumps(dados))



    if Participantes.objects.filter(cod_hist = cod_historia, cod_escrit = escritor.cod_escrit):
        sequencia_escritor = Participantes.objects.filter(cod_hist = cod_historia, cod_escrit = escritor.cod_escrit)[0].seq_particip
    else:
        dados = {   "acesso" : 'negado',
                    "message" : 'O escritor selecionado não participa dessa história.'
                }
        return HttpResponse(json.dumps(dados))



    if Partes.objects.filter(data_inicio = datetime.now, cod_escrit_id = escritor.id):
        dados = {   "acesso" : 'negado',
                    "message" : 'Esse escritor já contribuiu com essa história hoje.'
                }
        return HttpResponse(json.dumps(dados))
    


    return HttpResponse(json.dumps({ "acesso" : 'liberado' }))



def salvar_edicao(request):
    descricao = request.POST.get('descricao_historia', '')

    if descricao:
        print('entrou')
        escritor= Escritores.objects.get(cod_escrit = request.POST['cod_escrit'])
        historia = Historia.objects.get(cod_hist = request.POST['cod_hist'])
    
        parte = Partes()
        parte.cod_escrit = escritor
        parte.cod_hist = historia
        parte.desc_parte = descricao
    
        parte.save()
        return render(
            request,
            'app/editar_historia.html',
            context_instance = RequestContext(request,
            {
                'historias': Historia.objects.all(),
                'escritores': Escritores.objects.all(),
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
                'escritores': Escritores.objects.all(),
                'mensage': 'Favor preencher a descrição da história',
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
