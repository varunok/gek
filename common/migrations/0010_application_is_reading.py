# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20170514_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_reading',
            field=models.BooleanField(default=False),
        ),
    ]
