# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escritores',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cod_escrit', models.CharField(max_length=2)),
                ('nome_escrit', models.CharField(max_length=30)),
                ('email_escrit', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Escritores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cod_hist', models.CharField(max_length=1)),
                ('tit_hist', models.TextField(max_length=100)),
                ('prim_parag', models.TextField(max_length=600)),
            ],
            options={
                'db_table': 'Historia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('data_inicio', models.DateField(default=datetime.datetime.now, editable=False)),
                ('desc_parte', models.TextField(max_length=600)),
                ('cod_escrit', models.ForeignKey(to='app.Escritores')),
                ('cod_hist', models.ForeignKey(to='app.Historia')),
            ],
            options={
                'db_table': 'Partes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('seq_particip', models.CharField(max_length=1)),
                ('cod_escrit', models.ForeignKey(to='app.Escritores')),
                ('cod_hist', models.ForeignKey(to='app.Historia')),
            ],
            options={
                'db_table': 'Participantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Regras',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cod_regra', models.CharField(max_length=1)),
                ('desc_regra', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Regras',
            },
            bases=(models.Model,),
        ),
    ]
