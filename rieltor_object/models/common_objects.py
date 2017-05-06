# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TypeDeal(object):
    RENT = 'rent'
    SALE = 'sale'
    CHOICES = (
        (RENT, 'Аренда'),
        (SALE, 'Продажа')
    )


class TypeAppointment(object):
    APARTMENT = 'apartment'
    HOUSE = 'house'
    CHOICES = (
        (APARTMENT, 'Квартира'),
        (HOUSE, 'Дом')
    )


class TypeStatus(object):
    VIP = 'vip'
    DEFAULT = 'default'
    SHORT = 'short'
    CHOICES = (
        (VIP, 'VIP'),
        (DEFAULT, 'Обычное'),
        (SHORT, 'Краткое'),
    )


class TypeLocation(object):
    FACADE = 'facade'
    COURTYARD = 'from_yard'
    BISNESS = 'business_center'
    CHOICES = (
        (FACADE, 'Фасад'),
        (COURTYARD, 'Дворовой'),
        (BISNESS, 'Бизнес-центр'),
    )


class TypeFloor(object):
    FIRST = 'first'
    BASE = 'base'
    BELTAG = 'mezzanine'
    CHOICES = (
        (FIRST, '1-й'),
        (BASE, 'Цоколь'),
        (BELTAG, 'Бельэтаж'),
    )


class TypeEntrance(object):
    FACADE = 'facade'
    COURTYARD = 'from_yard'
    PARAD = 'with_grand'
    CHOICES = (
        (FACADE, 'Фасад'),
        (COURTYARD, 'Со двора'),
        (PARAD, 'С парадной'),
    )


class TypeArea(object):
    FOR_BUILDING = 'for_building'
    GARDENING = 'gardening'
    COMMERCIAL = 'commercial'
    HANDED = 'handed'
    CHOICES = (
        (FOR_BUILDING, 'Под застройку'),
        (GARDENING, 'Садоводство'),
        (COMMERCIAL, 'Комерческая'),
        (HANDED, 'Дом сдан'),
    )


class Communications(object):
    WATER = 'water'
    GAS = 'gas'
    SEWERAGE = 'sewage'
    ELECTRICITY = 'electricity'
    CHOICES = (
        (WATER, 'Вода'),
        (GAS, 'Газ'),
        (SEWERAGE, 'Канализация'),
        (ELECTRICITY, 'Электричество'),
    )


class StructureHouse(object):
    HOUSE = 'house'
    CUISINE = 'cuisine'
    BARN = 'barn'
    POOL = 'pool'
    CHOICES = (
        (HOUSE, 'Дом'),
        (CUISINE, 'Летная кухня'),
        (BARN, 'Сарай'),
        (POOL, 'Бассейн'),
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


class EarthDistrict(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = 'Район для земля'
        verbose_name_plural = 'Районы для земля'

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