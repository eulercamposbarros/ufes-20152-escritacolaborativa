from django.shortcuts import render, render_to_response
from django.core.context_processors import request, csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError 
from ahcoop.models import *
from django.contrib.auth import authenticate, logout, login
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from genericpath import exists
from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict
from django.http import HttpResponse
from random import *
import json



from django.shortcuts import render

# Create your views here.


def redireciona(request):
    return HttpResponseRedirect(reverse('ahcoop.views.inicio')) 

def inicio(request):  
    return render_to_response('inicio.html')

def adminesp(request):  
    return render_to_response('adminesp.html')

def regras(request):  
    regras = Regras.objects.all().order_by('cod_regra')
    return render_to_response('regras.html',{'regras' : regras})
  
def primParagraf(request):  
    historias = Historia.objects.all().order_by('cod_hist')
    return render_to_response('prim_paragraf.html',{'historias' : historias})

def proxParte(request):  
    proxparte = Partes.objects.all().order_by('cod_hist', 'cod_escrit', 'cod_parte')
    return render_to_response('proxparte.html',{'proxparte' : proxparte})