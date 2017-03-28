# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0004_auto_20170319_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('subtitle', models.TextField(blank=True, null=True, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('SEOTitle', models.TextField(blank=True, null=True, verbose_name='SEO Title')),
                ('SEOKeywords', models.TextField(blank=True, null=True, verbose_name='SEO Keywords')),
                ('SEODescription', models.TextField(blank=True, null=True, verbose_name='SEO Description')),
                ('is_eneble', models.BooleanField(default=True, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0435\u043d \u043b\u0438?')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0438',
            },
        ),
    ]