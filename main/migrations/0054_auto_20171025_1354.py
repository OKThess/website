# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20171025_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
