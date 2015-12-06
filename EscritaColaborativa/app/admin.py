# -*- coding: utf-8 -*-

from django.contrib import admin
from app.models import *
# Register your models here.
admin.site.register(Regras)
admin.site.register(Partes)


@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    ordering = ['tit_hist']
    list_display = ['cod_hist','get_title_historia', 'get_prim_parag']
    list_display_links = ['cod_hist','get_title_historia', 'get_prim_parag']

    def get_prim_parag(self,obj):
        return obj.prim_parag


    def get_title_historia(sel, obj):
        return obj.tit_hist

    get_title_historia.short_description = 'Título História'
    get_prim_parag.short_description ='Primeiro Paragrafo'



@admin.register(Escritores)
class EscritoresAdmin(admin.ModelAdmin):
    ordering = ['cod_escrit']
    list_display = ['cod_escrit','get_nome_escrit', 'get_email_escrit']
    list_display_links = ['cod_escrit','get_nome_escrit', 'get_email_escrit']

    def get_nome_escrit(self,obj):
        return obj.nome_escrit 

    def get_email_escrit(self,obj):
        return obj.email_escrit

    def cod_escrit(self,obj):
        return obj.cod_escrit    

    get_nome_escrit.short_description = 'Escritor'
    get_email_escrit.short_description ='E-mail'


@admin.register(Participantes)
class ParticipantesAdmin(admin.ModelAdmin):
    
    list_display = ['get_seq_particip','obtem_nome_escrito', 'get_cod_hist']
    list_display_links = ['get_seq_particip','obtem_nome_escrito', 'get_cod_hist']

    def get_seq_particip(self, obj):
        return obj.seq_particip

    def obtem_nome_escrito(self, obj):
        return obj.cod_escrit.nome_escrit

    def get_cod_hist(self, obj):
        return obj.cod_hist.tit_hist
  
    obtem_nome_escrito.short_description ='Escritor'
    get_cod_hist.short_description ='História'
    get_seq_particip.short_description = 'Ordem'



