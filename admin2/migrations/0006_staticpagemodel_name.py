# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0005_staticpagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpagemodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
