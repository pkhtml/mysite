# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-06-29 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160628_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type_db',
            old_name='type',
            new_name='urltype',
        ),
        migrations.RenameField(
            model_name='url_db',
            old_name='type',
            new_name='urltype',
        ),
    ]
