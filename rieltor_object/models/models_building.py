# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

# Create your models here.
from django.urls import reverse

from common.models import Photo, Video


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


class Building(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
        blank=True,
        null=True
    )
    SEOTitle = models.TextField(
        verbose_name='SEO Title',
        blank=True,
        null=True
    )
    SEOKeywords = models.TextField(
        verbose_name='SEO Keywords',
        blank=True,
        null=True
    )
    SEODescription = models.TextField(
        verbose_name='SEO Description',
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=250,
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name='Цена',
        blank=True,
        null=True
    )
    type_deal = models.IntegerField(
        verbose_name='Тип',
        choices=TypeDeal.CHOICES,
        blank=True,
        null=True
    )
    appointment = models.IntegerField(
        verbose_name='Назначение',
        choices=TypeAppointment.CHOICES,
        blank=True,
        null=True
    )
    footage = models.IntegerField(
        verbose_name='Площадь',
        blank=True,
        null=True
    )
    rooms = models.IntegerField(
        verbose_name='Комнат',
        blank=True,
        null=True
    )
    point = models.IntegerField(
        verbose_name='Балы',
        blank=True,
        null=True
    )
    when_create = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )
    location = models.IntegerField(
        verbose_name='Расположение',
        choices=TypeLocation.CHOICES,
        blank=True,
        null=True
    )
    floor = models.IntegerField(
        verbose_name='Этаж',
        choices=TypeFloor.CHOICES,
        blank=True,
        null=True
    )
    entrance = models.IntegerField(
        verbose_name='Вход',
        choices=TypeEntrance.CHOICES,
        blank=True,
        null=True
    )
    status = models.IntegerField(
        verbose_name='Статус',
        choices=TypeStatus.CHOICES,
        blank=True,
        null=True
    )
    district = models.ForeignKey(
        District,
        verbose_name='Район',
        on_delete=models.SET_NULL,
        related_name='building',
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    panorama = models.TextField(
        verbose_name='Панорама',
        blank=True
    )
    geo = models.TextField(
        verbose_name='На карте',
        blank=True
    )
    views = models.IntegerField(
        verbose_name='Просмотры',
        default=0
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    videos = GenericRelation(Video, related_query_name='building')
    images = GenericRelation(Photo, related_query_name='building')

    class Meta:
        verbose_name = 'Квартиры и Дома'
        verbose_name_plural = 'Квартиры и Дома'
        ordering = ['-when_create']

    def __unicode__(self):
        return '{0}'.format(self.id)

    def save(self, *args, **kwargs):
        if self.title:
            self.SEOTitle = self.title
            self.SEOKeywords = self.title
            self.SEODescription = '{0} {1} {2} {3} {4}'.format(self.get_type_deal_display(),
                                                               self.get_appointment_display(), self.address, self.price,
                                                               self.title)
        super(Building, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('admin2:building_edit', args=[self.id])

    def get_absolute_url(self):
        return reverse('objects:buildings_detail', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:buildings')

    def meta(self):
        return self._meta
