# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0006_auto_20170509_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsfranchise',
            name='price_180',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c 180 \u0434\u043d\u0435\u0439'),
        ),
        migrations.AlterField(
            model_name='settingsfranchise',
            name='price_30',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c 30 \u0434\u043d\u0435\u0439'),
        ),
        migrations.AlterField(
            model_name='settingsfranchise',
            name='price_90',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c 90 \u0434\u043d\u0435\u0439'),
        ),
    ]