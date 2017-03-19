# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel


class Settings(SingletonModel):
    UAH = 'UAH'
    RUB = 'RUB'
    KZT = 'KZT'
    CARRENCY = (
        (UAH, 'грн'),
        (RUB, 'руб'),
        (KZT, 'тнг')
    )
    currency = models.CharField(
        verbose_name='Валюта',
        choices=CARRENCY,
        max_length=3,
        blank=True
    )
    dollar_rate = models.FloatField(
        verbose_name='Курс доллара',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
