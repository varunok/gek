# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20170309_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='title',
            field=models.CharField(default=1, max_length=150, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
