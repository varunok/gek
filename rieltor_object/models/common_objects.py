# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TypeDeal(object):
    RENT = 'Аренда'
    SALE = 'Продажа'
    CHOICES = (
        (RENT, 'Аренда'),
        (SALE, 'Продажа')
    )


class TypeAppointment(object):
    APARTMENT = 'Квартира'
    HOUSE = 'Дом'
    CHOICES = (
        (APARTMENT, 'Квартира'),
        (HOUSE, 'Дом')
    )


class TypeStatus(object):
    VIP = 'VIP'
    DEFAULT = 'Обычное'
    SHORT = 'Краткое'
    CHOICES = (
        (VIP, 'VIP'),
        (DEFAULT, 'Обычное'),
        (SHORT, 'Краткое'),
    )


class TypeLocation(object):
    FACADE = 'Фасад'
    COURTYARD = 'Дворовой'
    BISNESS = 'Бизнес-центр'
    CHOICES = (
        (FACADE, 'Фасад'),
        (COURTYARD, 'Дворовой'),
        (BISNESS, 'Бизнес-центр'),
    )


class TypeFloor(object):
    FIRST = '1-й'
    COKOL = 'Цоколь'
    BELTAG = 'Бельэтаж'
    CHOICES = (
        (FIRST, '1-й'),
        (COKOL, 'Цоколь'),
        (BELTAG, 'Бельэтаж'),
    )


class TypeEntrance(object):
    FACADE = 'Фасад'
    COURTYARD = 'Со двора'
    PARAD = 'С парадной'
    CHOICES = (
        (FACADE, 'Фасад'),
        (COURTYARD, 'Со двора'),
        (PARAD, 'С парадной'),
    )


class District(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __unicode__(self):
        return self.name


class DailyDistrict(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = 'Район для посуточно'
        verbose_name_plural = 'Районы для посуточно'

    def __unicode__(self):
        return self.name


class ApartmentHas(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = 'В квартире есть'
        verbose_name_plural = 'В квартире есть'

    def __unicode__(self):
        return self.name


class ModelIn(object):
    model_in = (
        'newbuilding',
    )


class Infrastructure(models.Model):
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='icons/%Y/%m/%d/',
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
    )

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктура'
        ordering = ['-id']

    def __unicode__(self):
        return '{}'.format(self.title)


class Accommodations(models.Model):
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='icons/%Y/%m/%d/',
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=250,
    )

    class Meta:
        verbose_name = 'Условия проживания'
        verbose_name_plural = 'Условия проживания'

    def __unicode__(self):
        return '{}'.format(self.title)