# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0015_auto_20170427_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpagemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]
