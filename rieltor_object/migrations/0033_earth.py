# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0032_auto_20170425_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('SEOTitle', models.TextField(blank=True, null=True, verbose_name='SEO Title')),
                ('SEOKeywords', models.TextField(blank=True, null=True, verbose_name='SEO Keywords')),
                ('SEODescription', models.TextField(blank=True, null=True, verbose_name='SEO Description')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='\u0426\u0435\u043d\u0430')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('type_area', models.CharField(blank=True, choices=[('\u041f\u043e\u0434 \u0437\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0443', '\u041f\u043e\u0434 \u0437\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0443'), ('\u0421\u0430\u0434\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e', '\u0421\u0430\u0434\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e'), ('\u041a\u043e\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0430\u044f', '\u041a\u043e\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0430\u044f'), ('\u0414\u043e\u043c \u0441\u0434\u0430\u043d', '\u0414\u043e\u043c \u0441\u0434\u0430\u043d')], max_length=50, null=True, verbose_name='\u0422\u0438\u043f \u0423\u0447\u0430\u0441\u0442\u043a\u0430')),
                ('to_city', models.IntegerField(blank=True, null=True, verbose_name='\u0414\u043e \u0433\u043e\u0440\u043e\u0434\u0430')),
                ('area', models.IntegerField(blank=True, null=True, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('contact_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0435 \u043b\u0438\u0446\u043e')),
                ('phone', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('description', models.TextField(blank=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('geo', models.TextField(blank=True, verbose_name='\u041d\u0430 \u043a\u0430\u0440\u0442\u0435')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('when_create', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('communication', models.ManyToManyField(blank=True, related_name='earth', to='rieltor_object.Communications', verbose_name='\u041a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='earth', to='rieltor_object.EarthDistrict', verbose_name='\u0420\u0430\u0439\u043e\u043d')),
                ('structure_house', models.ManyToManyField(blank=True, related_name='earth', to='rieltor_object.StructureHouse', verbose_name='\u0421\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0434\u043e\u043c\u0430')),
            ],
            options={
                'ordering': ['-when_create'],
                'verbose_name': '\u0417\u0435\u043c\u043b\u044f',
                'verbose_name_plural': '\u0417\u0435\u043c\u043b\u044f',
            },
        ),
    ]