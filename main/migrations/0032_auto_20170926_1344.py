# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 13:44
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20170925_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_el',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
