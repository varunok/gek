# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0006_auto_20170514_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earth',
            name='phone1',
        ),
        migrations.AlterField(
            model_name='earth',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='earth', to='rieltor_object.Phone', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]
