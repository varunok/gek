# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0037_counters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('vodeo', models.TextField(blank=True, null=True, verbose_name='\u041a\u043e\u0434 \u0432\u0438\u0434\u0435\u043e')),
            ],
            options={
                'verbose_name': '\u0412\u0438\u0434\u0435\u043e',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e',
            },
        ),
    ]
