# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0004_remove_building_geo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='price_nac',
        ),
        migrations.AlterField(
            model_name='building',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0426\u0435\u043d\u0430'),
        ),
    ]