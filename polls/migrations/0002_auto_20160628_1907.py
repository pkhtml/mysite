# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-06-28 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_db',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='url_db',
            name='view_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
