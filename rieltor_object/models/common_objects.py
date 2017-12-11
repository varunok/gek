# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class TypeDeal(object):
    RENT = 'rent'
    SALE = 'sale'
    CHOICES = (
        (RENT, _('Аренда')),
        (SALE, _('Продажа'))
    )


class TypeAppointment(object):
    APARTMENT = 'apartment'
    HOUSE = 'house'
    ROOM = 'room'
    CHOICES = (
        (APARTMENT, _('Квартира')),
        (HOUSE, _('Дом')),
        (ROOM, _('Комната')),
    )


class TypeAppointmentOffice(object):
    OFFICE = 'office'
    SHOP = 'shop'
    CHOICES = (
        (OFFICE, _('Офис')),
        (SHOP, _('Магазин'))
    )


class TypeStatus(object):
    VIP = 'vip'
    DEFAULT = 'default'
    SHORT = 'short'
    CHOICES = (
        (VIP, 'VIP'),
        (DEFAULT, _('Обычное')),
        (SHORT, _('Краткое')),
    )


class TypeLocation(object):
    FACADE = 'facade'
    COURTYARD = 'from_yard'
    BISNESS = 'business_center'
    ALONEBUILD = 'alonebuild'
    CHOICES = (
        (FACADE, _('Фасад')),
        (COURTYARD, _('Дворовой')),
        (BISNESS, _('Бизнес-центр')),
        (ALONEBUILD, _('Отдельное здание')),
    )


class TypeLayout(object):
    RELATED = 'related'
    SEPARATE = 'separate'
    RELATED_SEPARATE = 'related-separate'
    CHOICES = (
        (RELATED, _('Смежные')),
        (SEPARATE, _('Раздельные')),
        (RELATED_SEPARATE, _('Смежно-раздельные')),
    )


class TypeFloor(object):
    FIRST = 'first'
    BASE = 'base'
    BELTAG = 'mezzanine'
    TWOFIVE = 'twofive'
    CHOICES = (
        (FIRST, _('1-й')),
        (BASE, _('Цоколь')),
        (BELTAG, _('Бельэтаж')),
        (TWOFIVE, _('2-5 этаж')),
    )


class TypeEntrance(object):
    FACADE = 'facade'
    COURTYARD = 'from_yard'
    PARAD = 'with_grand'
    CHOICES = (
        (FACADE, _('Фасад')),
        (COURTYARD, _('Со двора')),
        (PARAD, _('С парадной')),
    )


class TypeArea(object):
    FOR_BUILDING = 'for_building'
    GARDENING = 'gardening'
    COMMERCIAL = 'commercial'
    HANDED = 'handed'
    CHOICES = (
        (FOR_BUILDING, _('Под застройку')),
        (GARDENING, _('Садоводство')),
        (COMMERCIAL, _('Комерческая')),
        (HANDED, _('Дом сдан')),
    )


class Communications(object):
    WATER = 'water'
    GAS = 'gas'
    SEWERAGE = 'sewage'
    ELECTRICITY = 'electricity'
    CHOICES = (
        (WATER, _('Вода')),
        (GAS, _('Газ')),
        (SEWERAGE, _('Канализация')),
        (ELECTRICITY, _('Электричество')),
    )


class StructureHouse(object):
    HOUSE = 'house'
    CUISINE = 'cuisine'
    BARN = 'barn'
    POOL = 'pool'
    CHOICES = (
        (HOUSE, _('Дом')),
        (CUISINE, _('Летная кухня')),
        (BARN, _('Сарай')),
        (POOL, _('Бассейн')),
    )


class DistrictManager(models.Manager):
    def get_list_url(self):
        return reverse('admin2:district_list')


class District(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=250,
        unique=True
    )

    objects = DistrictManager()

    class Meta:
        verbose_name = _('Район')
        verbose_name_plural = _('Районы')

    def __unicode__(self):
        return self.name

    def get_edit_url(self):
        return reverse('admin2:district_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:district_delete', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:district_list')


class Name(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = _('Имя')
        verbose_name_plural = _('Имена')

    def __unicode__(self):
        return self.name


class Phone(models.Model):
    phone = models.CharField(
        verbose_name=_('Телефон'),
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = _('Телефон')
        verbose_name_plural = _('Телефон')

    def __unicode__(self):
        return self.phone


class DailyDistrictManager(models.Manager):
    def get_list_url(self):
        return reverse('admin2:district_list')


class DailyDistrict(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=250,
        unique=True
    )

    objects = DailyDistrictManager()

    class Meta:
        verbose_name = _('Район для посуточно')
        verbose_name_plural = _('Районы для посуточно')

    def __unicode__(self):
        return self.name

    def get_edit_url(self):
        return reverse('admin2:district_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:district_delete', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:district_list')


class EarthDistrictManager(models.Manager):
    def get_list_url(self):
        return reverse('admin2:district_list')


class EarthDistrict(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=250,
        unique=True
    )

    objects = EarthDistrictManager()

    class Meta:
        verbose_name = _('Район для земля')
        verbose_name_plural = _('Районы для земля')

    def __unicode__(self):
        return self.name

    def get_edit_url(self):
        return reverse('admin2:district_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:district_delete', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:district_list')


class ApartmentHas(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=250,
        unique=True
    )

    class Meta:
        verbose_name = _('В квартире есть')
        verbose_name_plural = _('В квартире есть')

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
        verbose_name=_('Заголовок'),
        max_length=250,
    )

    class Meta:
        verbose_name = _('Инфраструктура')
        verbose_name_plural = _('Инфраструктура')
        ordering = ['-id']

    def __unicode__(self):
        return '{}'.format(self.title)


class Accommodations(models.Model):
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='icons/%Y/%m/%d/',
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=250,
    )
    description = models.CharField(
        verbose_name=_('Описание'),
        max_length=250,
    )

    class Meta:
        verbose_name = _('Условия проживания')
        verbose_name_plural = _('Условия проживания')

    def __unicode__(self):
        return '{}'.format(self.title)