# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0026_auto_20170515_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildingpagemodel',
            old_name='title_h1',
            new_name='title',
        ),
    ]
