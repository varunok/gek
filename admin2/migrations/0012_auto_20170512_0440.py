# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0011_settingsliqpay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settingsliqpay',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='settingsprivate24',
            name='currency',
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='video',
            field=models.TextField(blank=True, verbose_name='\u041a\u043e\u0434 \u0432\u0438\u0434\u0435\u043e'),
        ),
        migrations.AddField(
            model_name='settingsfranchise',
            name='currency',
            field=models.CharField(blank=True, choices=[('UAH', 'UAH'), ('RUB', 'RUB'), ('USD', 'USD')], max_length=3, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='settingsliqpay',
            name='merchant',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Liqpay merchant ID'),
        ),
    ]
