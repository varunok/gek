# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
# from django.urls import reverse

from admin2.models import SettingsAddress, Settings
from common.models import Photo, Video
from rieltor_object.models.common_objects import *
from django.utils.translation import ugettext_lazy as _


class OficeManager(models.Manager):
    def vips(self, *args, **kwargs):
        kwargs['is_vip'] = True
        return self.filter(*args, **kwargs)


class Ofice(models.Model):
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
    address = models.CharField(
        verbose_name=_('Адрес'),
        max_length=250,
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name=_('Цена'),
        blank=True,
        null=True
    )
    type_deal = models.CharField(
        verbose_name=_('Тип'),
        max_length=20,
        choices=TypeDeal.CHOICES,
        blank=True,
        null=True
    )
    appointment = models.CharField(
        verbose_name=_('Назначение'),
        max_length=20,
        choices=TypeAppointmentOffice.CHOICES,
        blank=True,
        null=True
    )
    footage = models.IntegerField(
        verbose_name=_('Площадь'),
        blank=True,
        null=True
    )
    rooms = models.IntegerField(
        verbose_name=_('Комнат'),
        blank=True,
        null=True
    )
    point = models.IntegerField(
        verbose_name=_('Балы'),
        blank=True,
        null=True
    )
    when_create = models.DateTimeField(
        verbose_name=_('Дата публикации'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('Дата редактирования'),
        auto_now=True
    )
    location = models.CharField(
        verbose_name=_('Расположение'),
        max_length=20,
        choices=TypeLocation.CHOICES,
        blank=True,
        null=True
    )
    floor = models.CharField(
        verbose_name=_('Этаж'),
        max_length=20,
        choices=TypeFloor.CHOICES,
        blank=True,
        null=True
    )
    entrance = models.CharField(
        verbose_name=_('Вход'),
        max_length=20,
        choices=TypeEntrance.CHOICES,
        blank=True,
        null=True
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('Район'),
        on_delete=models.SET_NULL,
        related_name='ofice',
        null=True,
        blank=True
    )
    name = models.ForeignKey(
        Name,
        verbose_name=_('Имя'),
        on_delete=models.SET_NULL,
        related_name='ofice',
        null=True,
        blank=True
    )
    phone = models.ForeignKey(
        Phone,
        verbose_name=_('Телефон'),
        on_delete=models.SET_NULL,
        related_name='ofice',
        null=True,
        blank=True
    )
    description = RichTextUploadingField(
        verbose_name=_('Описание'),
        blank=True
    )
    panorama = models.TextField(
        verbose_name=_('Панорама'),
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
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    is_vip = models.BooleanField(
        verbose_name='VIP',
        default=False
    )
    is_short = models.BooleanField(
        verbose_name=_('Краткое'),
        default=False
    )
    video = models.TextField(
        verbose_name=_('Код видео'),
        blank=True
    )
    images = GenericRelation(Photo, related_query_name='ofice')

    objects = OficeManager()

    class Meta:
        verbose_name = _('Офисы и магазины')
        verbose_name_plural = _('Офисы и магазины')
        ordering = ['-when_create']

    def __unicode__(self):
        if self.SEODescription:
            return '{0}'.format(self.SEODescription)
        return '{0}'.format(self.id)

    def save(self, *args, **kwargs):
        self.SEOTitle = self.normalize_SEO('{0} {1} по {2} ценна {3} в {4}'.format(self.get_type_deal_display() or '',
                                                     self.get_appointment_display() or '',
                                                     self.address or '',
                                                     self.price or '',
                                                     SettingsAddress.get_solo().city_plural or ''))
        self.SEODescription = self.normalize_SEO('{0} {1} {2} по {3} район {4}'.format(self.title or '',
                                                             self.get_type_deal_display() or '',
                                                             self.get_appointment_display() or '',
                                                             self.address or '',
                                                             self.district or ''))
        self.SEOKeywords = self.SEODescription
        super(Ofice, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('admin2:ofice_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:ofice_delete', args=[self.id])

    def get_absolute_url(self):
        return reverse('objects:ofice_detail', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:ofices')

    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__).id

    def meta(self):
        return self._meta

    def normalize_SEO(self, text):
        try:
            if settings.LANGUAGE_CODE == 'uk':
                text = text.replace('Офіс', 'офісу')
                text = text.replace('Магазин', 'магазину')
            elif settings.LANGUAGE_CODE == 'ru':
                text = text.replace('Офис', 'офиса')
                text = text.replace('Магазин', 'магазина')
        except AttributeError:
            pass
        return _(text)

    def get_title(self):
        appointment = self.normalize_SEO(self.get_appointment_display())
        return '{0} {1}'.format(self.get_type_deal_display() or '', appointment or '')

    def footage_price(self):
        if self.footage and self.price:
            return self.price // self.footage

    def get_current(self):
        if self.type_deal == TypeDeal.SALE:
            return '$'
        elif self.type_deal == TypeDeal.RENT:
            return Settings.get_solo().get_currency_display()
