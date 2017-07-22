# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
# from django.urls import reverse

from admin2.models import SettingsAddress
from common.models import Photo, Video
from rieltor_object.models.common_objects import *
from django.utils.translation import ugettext_lazy as _


class NewBuildingManager(models.Manager):
    def is_enable(self, *args, **kwargs):
        kwargs['is_enable'] = True
        return self.filter(*args, **kwargs)


class NewBuilding(models.Model):
    custom_id = models.PositiveIntegerField(
        verbose_name='ID',
        unique=True,
        blank=True,
        null=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        allow_unicode=True
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=250,
        blank=True,
        null=True
    )
    is_enable = models.BooleanField(
        verbose_name=_('Статус'),
        default=True,
        help_text=_('нужно сохранять')
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
        verbose_name=_('Адрес'),
        max_length=250,
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name=_('Цена за м.кв'),
        blank=True,
        null=True
    )
    price_object = models.IntegerField(
        verbose_name=_('Цена за объект'),
        blank=True,
        null=True
    )
    date_delivery = models.DateField(
        verbose_name=_('Дата сдачи'),
        blank=True,
        null=True
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('Район'),
        on_delete=models.SET_NULL,
        related_name='newbuilding',
        null=True,
        blank=True
    )
    name = models.ForeignKey(
        Name,
        verbose_name=_('Имя'),
        on_delete=models.SET_NULL,
        related_name='newbuilding',
        null=True,
        blank=True
    )
    phone = models.ForeignKey(
        Phone,
        verbose_name=_('Телефон'),
        on_delete=models.SET_NULL,
        related_name='newbuilding',
        null=True,
        blank=True
    )
    point = models.IntegerField(
        verbose_name=_('Балы'),
        blank=True,
        null=True
    )
    description = RichTextUploadingField(
        verbose_name=_('Описание'),
        blank=True
    )
    panorama = models.TextField(
        verbose_name=_('Панорама'),
        blank=True
    )
    geo = models.TextField(
        verbose_name=_('На карте'),
        blank=True
    )
    views = models.IntegerField(
        verbose_name=_('Просмотры'),
        default=0
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    when_create = models.DateTimeField(
        verbose_name=_('Дата публикации'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('Дата редактирования'),
        auto_now=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    parade = models.PositiveSmallIntegerField(
        verbose_name=_('Парадных'),
        blank=True,
        null=True
    )
    storeys = models.PositiveSmallIntegerField(
        verbose_name=_('Этажность'),
        blank=True,
        null=True
    )
    parking_places = models.PositiveSmallIntegerField(
        verbose_name=_('Парковочных мест'),
        blank=True,
        null=True
    )
    total_area = models.PositiveSmallIntegerField(
        verbose_name=_('Общая площадь'),
        blank=True,
        null=True
    )
    class_house = models.CharField(
        verbose_name=_('Клас дома'),
        max_length=20,
        blank=True,
        null=True
    )
    start_construction = models.DateField(
        verbose_name=_('Начало строительства'),
        blank=True,
        null=True
    )
    end_construction = models.DateField(
        verbose_name=_('Конец строительства'),
        blank=True,
        null=True
    )
    objects = NewBuildingManager()
    infrastructures = models.ManyToManyField(Infrastructure,
                                             related_name='newbuilding',
                                             blank=True
                                             )
    accommodations = models.ManyToManyField(Accommodations,
                                             related_name='newbuilding',
                                             blank=True
                                             )
    videos = GenericRelation(Video, related_query_name='newbuilding')
    images = GenericRelation(Photo, related_query_name='newbuilding')

    class Meta:
        verbose_name = _('Новострои')
        verbose_name_plural = _('Новострои')
        ordering = ['-when_create']

    def __unicode__(self):
        if self.SEODescription:
            return '{0}'.format(self.SEODescription)
        return '{0}'.format(self.id)

    def save(self, *args, **kwargs):
        self.SEOTitle = self.normalize_SEO('Продажа в новострое по {0} район {1} ценна {2} в {3}'.format(
                                                     self.address or '',
                                                     self.district or '',
                                                     self.price or '',
                                                     SettingsAddress.get_solo().city_plural or ''))
        self.SEODescription = self.normalize_SEO('Продажа в новострое по {0} район {1} в {2}'.format(
                                                     self.address or '',
                                                     self.district or '',
                                                     SettingsAddress.get_solo().city_plural or ''))
        self.SEOKeywords = self.SEODescription
        super(NewBuilding, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('admin2:newbuilding_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:newbuilding_delete', args=[self.id])

    def get_absolute_url(self):
        return reverse('objects:newbuilding_detail', args=[self.slug])

    def get_list_url(self):
        return reverse('admin2:newbuildings')

    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__).id

    def meta(self):
        return self._meta

    def normalize_SEO(self, text):
        return text
