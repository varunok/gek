# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_sections_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='URL'),
        ),
    ]
