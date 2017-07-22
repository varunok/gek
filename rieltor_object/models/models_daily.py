# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from admin2.models import SettingsAddress
from common.models import Photo, Video, ApartmentNext
# from django.db import models
from rieltor_object.models.common_objects import *
from django.utils.translation import ugettext_lazy as _


class Daily(models.Model):
    custom_id = models.PositiveIntegerField(
        verbose_name='ID',
        unique=True,
        blank=True,
        null=True
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
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
        verbose_name=_('Цена'),
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name=_('Адрес'),
        max_length=250,
        blank=True,
        null=True
    )
    floor = models.IntegerField(
        verbose_name=_('Этаж'),
        blank=True,
        null=True
    )
    guest = models.IntegerField(
        verbose_name=_('Гостей'),
        blank=True,
        null=True
    )
    sleeping_places = models.IntegerField(
        verbose_name=_('Спальных мест'),
        blank=True,
        null=True
    )
    rooms = models.IntegerField(
        verbose_name=_('Комнат'),
        blank=True,
        null=True
    )
    description = RichTextUploadingField(
        verbose_name=_('Описание'),
        blank=True
    )
    district = models.ForeignKey(
        DailyDistrict,
        verbose_name=_('Район'),
        on_delete=models.SET_NULL,
        related_name='daily',
        null=True,
        blank=True
    )
    name = models.ForeignKey(
        Name,
        verbose_name=_('Имя'),
        on_delete=models.SET_NULL,
        related_name='daily',
        null=True,
        blank=True
    )
    phone = models.ForeignKey(
        Phone,
        verbose_name=_('Телефон'),
        on_delete=models.SET_NULL,
        related_name='daily',
        null=True,
        blank=True
    )
    panorama = models.TextField(
        verbose_name=_('Панорама'),
        blank=True
    )
    video = models.TextField(
        verbose_name=_('Код видео'),
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
    point = models.IntegerField(
        verbose_name=_('Балы'),
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
                                           verbose_name=_('В квартире есть'),
                                           help_text=_('Для создания значения начните набирать текст')
                                           )
    apartment_next = GenericRelation(ApartmentNext, related_query_name='daily')
    images = GenericRelation(Photo, related_query_name='daily')
    videos = GenericRelation(Video, related_query_name='daily')

    class Meta:
        verbose_name = _('Посуточно')
        verbose_name_plural = _('Посуточно')
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
                text = text.replace(_('комнаты'), _('комнат'))
            except AttributeError:
                pass
        return text

    def get_title(self):
        return '{0}{2} {1}'.format(self.title or '', self.address or '', '.' if self.title else '' )
