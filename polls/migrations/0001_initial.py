# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 03:51
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='\u0412\u0430\u0440\u0438\u0430\u043d\u0442')),
                ('ball', models.IntegerField(default=0, verbose_name='\u0411\u0430\u043b\u043b')),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('test_end', models.IntegerField(default=0, verbose_name='\u0422\u0435\u0441\u0442 \u043f\u0440\u043e\u0448\u043b\u043e')),
                ('image', models.ImageField(blank=True, upload_to='polls/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u0441\u0442',
                'verbose_name_plural': '\u0422\u0435\u0441\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('title_image', models.ImageField(blank=True, upload_to='result/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(blank=True, upload_to='result/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442')),
                ('ball_from', models.IntegerField(verbose_name='\u0411\u0430\u043b\u043b\u043e\u0432 \u041e\u0442')),
                ('ball_to', models.IntegerField(verbose_name='\u0411\u0430\u043b\u043b\u043e\u0432 \u0414\u043e')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442',
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='polls',
            name='questions',
            field=models.ManyToManyField(related_name='polls', to='polls.Question', verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441\u044b'),
        ),
        migrations.AddField(
            model_name='polls',
            name='results',
            field=models.ManyToManyField(related_name='polls', to='polls.Result', verbose_name='\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
