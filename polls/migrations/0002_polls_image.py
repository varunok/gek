# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='image',
            field=models.ImageField(blank=True, upload_to='polls/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
    ]