# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_okthessmeetup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('url', models.URLField()),
            ],
        ),
    ]
