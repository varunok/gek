# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.urls import reverse

from admin2.models import SettingsAddress, Settings
from common.models import Photo, Video
from rieltor_object.models.common_objects import *


class OficeManager(models.Manager):
    def vips(self, *args, **kwargs):
        kwargs['status'] = TypeStatus.VIP
        return self.filter(*args, **kwargs)


class Ofice(models.Model):
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
    type_deal = models.CharField(
        verbose_name='Тип',
        max_length=20,
        choices=TypeDeal.CHOICES,
        blank=True,
        null=True
    )
    appointment = models.CharField(
        verbose_name='Назначение',
        max_length=20,
        choices=TypeAppointmentOffice.CHOICES,
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
    location = models.CharField(
        verbose_name='Расположение',
        max_length=20,
        choices=TypeLocation.CHOICES,
        blank=True,
        null=True
    )
    floor = models.CharField(
        verbose_name='Этаж',
        max_length=20,
        choices=TypeFloor.CHOICES,
        blank=True,
        null=True
    )
    entrance = models.CharField(
        verbose_name='Вход',
        max_length=20,
        choices=TypeEntrance.CHOICES,
        blank=True,
        null=True
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=TypeStatus.CHOICES,
        blank=True,
        null=True
    )
    district = models.ForeignKey(
        District,
        verbose_name='Район',
        on_delete=models.SET_NULL,
        related_name='ofice',
        null=True,
        blank=True
    )
    name = models.ForeignKey(
        Name,
        verbose_name='Имя',
        on_delete=models.SET_NULL,
        related_name='ofice',
        null=True,
        blank=True
    )
    phone = models.ForeignKey(
        Phone,
        verbose_name='Телефон',
        on_delete=models.SET_NULL,
        related_name='ofice',
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    videos = GenericRelation(Video, related_query_name='ofice')
    images = GenericRelation(Photo, related_query_name='ofice')

    objects = OficeManager()

    class Meta:
        verbose_name = 'Офисы и магазины'
        verbose_name_plural = 'Офисы и магазины'
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
            text = text.replace('Офис', 'офиса')
            text = text.replace('Магазин', 'магазина')
        except AttributeError:
            pass
        return text

    def footage_price(self):
        if self.footage and self.price:
            return self.price // self.footage

    def get_current(self):
        if self.type_deal == TypeDeal.SALE:
            return '$'
        elif self.type_deal == TypeDeal.RENT:
            return Settings.get_solo().get_currency_display()
