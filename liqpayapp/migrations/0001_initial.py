# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiqPayTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=16, verbose_name='action')),
                ('payment_id', models.IntegerField(verbose_name='payment_id')),
                ('version', models.IntegerField(verbose_name='version')),
                ('amount', models.FloatField(verbose_name='amount')),
                ('sender_commission', models.FloatField(verbose_name='sender_commission')),
                ('receiver_commission', models.FloatField(verbose_name='receiver_commission')),
                ('agent_commission', models.FloatField(verbose_name='agent_commission')),
                ('sender_card_country', models.IntegerField(verbose_name='sender_card_country')),
                ('transaction_id', models.IntegerField(verbose_name='transaction_id')),
                ('status', models.CharField(max_length=16, verbose_name='status')),
                ('type', models.CharField(max_length=16, verbose_name='type')),
                ('paytype', models.CharField(max_length=16, verbose_name='paytype')),
                ('public_key', models.CharField(max_length=32, verbose_name='public_key')),
                ('acq_id', models.CharField(max_length=32, verbose_name='acq_id')),
                ('order_id', models.CharField(max_length=32, verbose_name='order_id')),
                ('liqpay_order_id', models.CharField(max_length=32, verbose_name='liqpay_order_id')),
                ('description', models.CharField(max_length=120, verbose_name='description')),
                ('sender_card_mask2', models.CharField(max_length=16, verbose_name='sender_card_mask2')),
                ('sender_card_bank', models.CharField(max_length=16, verbose_name='sender_card_bank')),
                ('sender_card_type', models.CharField(max_length=16, verbose_name='sender_card_type')),
                ('ip', models.CharField(max_length=16, verbose_name='ip')),
                ('currency', models.CharField(max_length=16, verbose_name='currency')),
                ('currency_debit', models.CharField(max_length=16, verbose_name='currency_debit')),
                ('create_date', models.CharField(max_length=64, verbose_name='create_date')),
                ('end_date', models.CharField(max_length=64, verbose_name='end_date')),

            ],
        ),
    ]
