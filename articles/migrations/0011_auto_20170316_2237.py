# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20170316_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='sections',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f'),
        ),
    ]