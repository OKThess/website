# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20170922_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='description_en',
            new_name='description_el',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='description_en',
            new_name='description_el',
        ),
    ]
