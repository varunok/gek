# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_application_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='custom_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID'),
        ),
    ]