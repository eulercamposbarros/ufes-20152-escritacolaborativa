from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Historia(models.Model):
    cod_hist = models.CharField(max_length = 1)
    tit_hist = models.TextField(max_length = 100)
    prim_parag = models.TextField(max_length = 600)
    
    def __str__(self):
        return self.tit_hist 

    class Meta:
        db_table = 'Historia'
        
class Escritores(models.Model):
    cod_escrit = models.CharField(max_length = 2)
    nome_escrit = models.CharField(max_length = 30)
    email_escrit = models.CharField(max_length = 300)
            
    def __str__(self):
        return self.nome_escrit

    class Meta:
        db_table = 'Escritores'

class Participantes(models.Model):
    cod_hist = models.ForeignKey(Historia)
    cod_escrit = models.ForeignKey(Escritores)
    seq_particip = models.CharField(max_length = 1)
  
    
    class Meta:
        db_table = 'Participantes'
        
class Regras(models.Model):
    cod_regra = models.CharField(max_length = 1)
    desc_regra = models.CharField(max_length = 100)
    
    
    class Meta:
        db_table = 'Regras'
        
class Partes(models.Model) :
    cod_hist = models.ForeignKey(Historia)
    cod_escrit = models.ForeignKey(Escritores)     
    data_inicio = models.DateField(default = datetime.now, editable=False)    
    desc_parte = models.TextField(max_length = 600)
    
    class Meta:
        db_table = 'Partes'