# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160629_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('ifuse', models.IntegerField()),
                ('model_1', models.CharField(max_length=3)),
                ('model_2', models.CharField(max_length=3)),
                ('expdate', models.DateTimeField()),
            ],
        ),
    ]
