# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escritores',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
            name='Participantes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('seq_particip', models.CharField(max_length=1)),
                ('cod_escrit', models.ForeignKey(to='ahcoop.Escritores')),
                ('cod_hist', models.ForeignKey(to='ahcoop.Historia')),
            ],
            options={
                'db_table': 'Participantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Regras',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cod_regra', models.CharField(max_length=1)),
                ('desc_regra', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Regras',
            },
            bases=(models.Model,),
        ),
    ]
