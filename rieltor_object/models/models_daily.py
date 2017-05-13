# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from admin2.models import SettingsAddress
from common.models import Photo, Video, ApartmentNext
# from django.db import models
from rieltor_object.models.common_objects import *


class Daily(models.Model):
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
    price = models.IntegerField(
        verbose_name='Цена',
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=250,
        blank=True,
        null=True
    )
    floor = models.IntegerField(
        verbose_name='Этаж',
        blank=True,
        null=True
    )
    guest = models.IntegerField(
        verbose_name='Гостей',
        blank=True,
        null=True
    )
    sleeping_places = models.IntegerField(
        verbose_name='Спальных мест',
        blank=True,
        null=True
    )
    rooms = models.IntegerField(
        verbose_name='Комнат',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    district = models.ForeignKey(
        DailyDistrict,
        verbose_name='Район',
        on_delete=models.SET_NULL,
        related_name='daily',
        null=True,
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
    when_create = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    point = models.IntegerField(
        verbose_name='Балы',
        blank=True,
        null=True
    )
    infrastructures = models.ManyToManyField(Infrastructure,
                                             related_name='daily',
                                             blank=True
                                             )
    apartment_has = models.ManyToManyField(ApartmentHas,
                                           related_name='daily',
                                           blank=True,
                                           verbose_name='В квартире есть',
                                           help_text='Для создания значения начните набирать текст'
                                           )
    apartment_next = GenericRelation(ApartmentNext, related_query_name='daily')
    images = GenericRelation(Photo, related_query_name='daily')
    videos = GenericRelation(Video, related_query_name='daily')

    class Meta:
        verbose_name = 'Посуточно'
        verbose_name_plural = 'Посуточно'
        ordering = ['-when_create']

    def __unicode__(self):
        if self.SEODescription:
            return '{0}'.format(self.SEODescription)
        return '{0}'.format(self.id)

    def save(self, *args, **kwargs):
        self.SEOTitle = self.normalize_SEO('Аренда {0} комнаты по {1} ценна {2} в {3}'.format(
                                                     self.rooms or '',
                                                     self.address or '',
                                                     self.price or '',
                                                     SettingsAddress.get_solo().city_plural or ''))
        self.SEODescription = self.normalize_SEO('Аренда {0} комнаты по {1} район {2} в {3}'.format(
                                                     self.rooms or '',
                                                     self.address or '',
                                                     self.district or '',
                                                     SettingsAddress.get_solo().city_plural or ''))
        self.SEOKeywords = self.SEODescription
        super(Daily, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('admin2:daily_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:daily_delete', args=[self.id])

    def get_absolute_url(self):
        return reverse('objects:daily_detail', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:dailys')

    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__).id

    def meta(self):
        return self._meta

    def normalize_SEO(self, text):
        if self.rooms > 1:
            try:
                text = text.replace('комнаты', 'комнат')
            except AttributeError:
                pass
        return text
