# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0004_auto_20170508_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveFranchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_franchise', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SettingsFranchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_30', models.PositiveSmallIntegerField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c 30 \u0434\u043d\u0435\u0439')),
                ('price_90', models.PositiveSmallIntegerField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c 90 \u0434\u043d\u0435\u0439')),
                ('price_180', models.PositiveSmallIntegerField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c 180 \u0434\u043d\u0435\u0439')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u044b',
                'verbose_name_plural': '\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u044b',
            },
        ),
        migrations.AlterField(
            model_name='settingsaddress',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=' \u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]
