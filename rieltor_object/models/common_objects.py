# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TypeDeal(object):
    RENT = 1
    SALE = 2
    CHOICES = (
        (RENT, 'Аренда'),
        (SALE, 'Продажа')
    )


class TypeAppointment(object):
    APARTMENT = 1
    HOUSE = 2
    CHOICES = (
        (APARTMENT, 'Квартира'),
        (HOUSE, 'Дом')
    )


class TypeStatus(object):
    VIP = 1
    DEFAULT = 2
    SHORT = 3
    CHOICES = (
        (VIP, 'VIP'),
        (DEFAULT, 'Обычное'),
        (SHORT, 'Краткое'),
    )


class TypeLocation(object):
    FACADE = 1
    COURTYARD = 2
    BISNESS = 3
    CHOICES = (
        (FACADE, 'Фасад'),
        (COURTYARD, 'Дворовой'),
        (BISNESS, 'Бизнес-центр'),
    )


class TypeFloor(object):
    FIRST = 1
    COKOL = 2
    BELTAG = 3
    CHOICES = (
        (FIRST, '1-й'),
        (COKOL, 'Цоколь'),
        (BELTAG, 'Бельэтаж'),
    )


class TypeEntrance(object):
    FACADE = 1
    COURTYARD = 2
    PARAD = 3
    CHOICES = (
        (FACADE, 'Фасад'),
        (COURTYARD, 'Со двора'),
        (PARAD, 'С парадной'),
    )


class District(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250
    )

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __unicode__(self):
        return self.name