# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_auto_20171025_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]