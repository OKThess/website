# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 13:49
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_applytext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applytext',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
