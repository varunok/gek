# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 19:52
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_sections_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]