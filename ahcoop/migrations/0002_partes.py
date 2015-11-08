# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahcoop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partes',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('cod_parte', models.CharField(max_length=1)),
                ('data_iniparte', models.DateField()),
                ('hora_iniparte', models.TimeField()),
                ('data_fimparte', models.DateField()),
                ('hora_fimparte', models.TimeField()),
                ('desc_parte', models.TextField(max_length=600)),
                ('cod_escrit', models.ForeignKey(to='ahcoop.Escritores')),
                ('cod_hist', models.ForeignKey(to='ahcoop.Historia')),
            ],
            options={
                'db_table': 'Partes',
            },
            bases=(models.Model,),
        ),
    ]
