# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('common', '0012_feed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a', '\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), ('\u0412\u0442\u043e\u0440\u043d\u0438\u043a', '\u0412\u0442\u043e\u0440\u043d\u0438\u043a'), ('\u0421\u0440\u0435\u0434\u0430', '\u0421\u0440\u0435\u0434\u0430'), ('\u0427\u0435\u0442\u0432\u0435\u0440\u0433', '\u0427\u0435\u0442\u0432\u0435\u0440\u0433'), ('\u041f\u044f\u0442\u043d\u0438\u0446\u0430', '\u041f\u044f\u0442\u043d\u0438\u0446\u0430'), ('\u0421\u0443\u0431\u0431\u043e\u0442\u0430', '\u0421\u0443\u0431\u0431\u043e\u0442\u0430'), ('\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435', '\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435')], max_length=25, null=True, verbose_name='\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438')),
                ('open_from', models.TimeField(blank=True, null=True, verbose_name='\u0427\u0430\u0441\u043e\u0432 \u041e\u0442')),
                ('open_to', models.TimeField(blank=True, null=True, verbose_name='\u0427\u0430\u0441\u043e\u0432 \u0414\u043e')),
                ('special', models.CharField(blank=True, help_text='\u0414\u0440\u0443\u0433\u043e\u0435 \u0431\u0443\u0434\u0435\u0442 \u0438\u0433\u043d\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u0441\u044f', max_length=250, null=True, verbose_name='C\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0430\u0444\u0438\u043a \u0440\u0430\u0431\u043e\u0442\u044b',
                'verbose_name_plural': '\u0413\u0440\u0430\u0444\u0438\u043a \u0440\u0430\u0431\u043e\u0442\u044b',
            },
        ),
    ]
