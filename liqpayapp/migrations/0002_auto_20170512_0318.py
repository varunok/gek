# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liqpayapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liqpaytransaction',
            name='create_date',
            field=models.CharField(max_length=64, verbose_name='create_date'),
        ),
        migrations.AlterField(
            model_name='liqpaytransaction',
            name='end_date',
            field=models.CharField(max_length=64, verbose_name='end_date'),
        ),
    ]