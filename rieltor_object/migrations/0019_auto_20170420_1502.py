# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0018_auto_20170418_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='type_deal',
            field=models.IntegerField(blank=True, choices=[('\u0410\u0440\u0435\u043d\u0434\u0430', '\u0410\u0440\u0435\u043d\u0434\u0430'), ('\u041f\u0440\u043e\u0434\u0430\u0436\u0430', '\u041f\u0440\u043e\u0434\u0430\u0436\u0430')], null=True, verbose_name='\u0422\u0438\u043f'),
        ),
        migrations.AlterField(
            model_name='ofice',
            name='type_deal',
            field=models.IntegerField(blank=True, choices=[('\u0410\u0440\u0435\u043d\u0434\u0430', '\u0410\u0440\u0435\u043d\u0434\u0430'), ('\u041f\u0440\u043e\u0434\u0430\u0436\u0430', '\u041f\u0440\u043e\u0434\u0430\u0436\u0430')], null=True, verbose_name='\u0422\u0438\u043f'),
        ),
    ]
