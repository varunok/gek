# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0031_auto_20170515_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trustpagemodel',
            old_name='title',
            new_name='title_seo',
        ),
    ]
