# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-30 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_auto_20171223_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]