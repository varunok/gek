# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0039_auto_20170528_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name=''),
        ),
    ]
