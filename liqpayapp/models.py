# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LiqPayTransaction(models.Model):
    action = models.CharField('action', max_length=16)
    payment_id = models.IntegerField('payment_id')
    version = models.IntegerField('version')
    amount = models.FloatField('amount')
    sender_commission = models.FloatField('sender_commission')
    receiver_commission = models.FloatField('receiver_commission')
    agent_commission = models.FloatField('agent_commission')
    sender_card_country = models.IntegerField('sender_card_country')
    transaction_id = models.IntegerField('transaction_id')
    status = models.CharField('status', max_length=16)
    type = models.CharField('type', max_length=16)
    paytype = models.CharField('paytype', max_length=16)
    public_key = models.CharField('public_key', max_length=32)
    acq_id = models.CharField('acq_id', max_length=32)
    order_id = models.CharField('order_id', max_length=32)
    liqpay_order_id = models.CharField('liqpay_order_id', max_length=32)
    description = models.CharField('description', max_length=120)
    sender_card_mask2 = models.CharField('sender_card_mask2', max_length=16)
    sender_card_bank = models.CharField('sender_card_bank', max_length=16)
    sender_card_type = models.CharField('sender_card_type', max_length=16)
    ip = models.CharField('ip', max_length=16)
    currency = models.CharField('currency', max_length=16)
    currency_debit = models.CharField('currency_debit', max_length=16)
    create_date = models.CharField('create_date', max_length=64)
    end_date = models.CharField('end_date', max_length=64)