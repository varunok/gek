# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0003_auto_20170515_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seo',
            old_name='content_seo',
            new_name='content',
        ),
    ]