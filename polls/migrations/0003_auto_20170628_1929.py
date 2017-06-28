# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_urlresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlresult',
            name='ball',
            field=models.IntegerField(default=11, verbose_name='\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urlresult',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='9msqflfr', unique=True, verbose_name='URL'),
        ),
    ]