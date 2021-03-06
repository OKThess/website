# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_auto_20171204_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='answer_idea_1',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_idea_2',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_idea_3',
            field=models.CharField(choices=[('idea', 'Idea'), ('prototype', 'Prototype'), ('users', 'Early users'), ('revenue', 'Early revenue')], default='idea', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_market_1',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_market_2',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_market_3',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_market_4',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_market_5',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_market_6',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_market_7',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_team_1',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_team_2',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_team_3',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_team_4',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_team_5',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_team_6',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='application',
            name='answer_team_7',
            field=models.TextField(default='default'),
        ),
    ]
