# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-29 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0022_auto_20170609_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='custom_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='ID'),
        ),
    ]