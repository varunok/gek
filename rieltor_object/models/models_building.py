# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse

from admin2.models import SettingsAddress, Settings
from common.models import Photo, Video
from rieltor_object.models.common_objects import *
from rieltor_object.models.models_newbuilding import NewBuilding
from django.utils.translation import ugettext_lazy as _


class Period(object):
    SHORT = 'short'
    MONTH = 'month'
    LONG = 'long'
    CHOICES = (
        (SHORT, _('короткий')),
        (MONTH, _('месяц')),
        (LONG, _('долгий срок (6мес)')),
    )


class Proposal(object):
    CONDO = 'condo'
    APARTMENT = 'appartment'
    VILLAS = 'villas'
    CHOICES = (
        (CONDO, _('кондо')),
        (APARTMENT, _('квартиры')),
        (VILLAS, _('виллы')),
    )


class BuildingManager(models.Manager):
    def vips(self, *args, **kwargs):
        kwargs['is_vip'] = True
        return self.filter(*args, **kwargs)

    def shorts(self, *args, **kwargs):
        kwargs['is_short'] = True
        return self.filter(*args, **kwargs)


class Building(models.Model):
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
        choices=TypeAppointment.CHOICES,
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
    layout = models.CharField(
        verbose_name=_('Планировка'),
        max_length=20,
        choices=TypeLayout.CHOICES,
        blank=True,
        null=True
    )
    floor = models.IntegerField(
        verbose_name=_('Этаж'),
        blank=True,
        null=True
    )
    is_vip = models.BooleanField(
        verbose_name='VIP',
        default=False
    )
    is_short = models.BooleanField(
        verbose_name=_('Краткое'),
        default=False
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('Район'),
        on_delete=models.SET_NULL,
        related_name='building',
        null=True,
        blank=True
    )
    name = models.ForeignKey(
        Name,
        verbose_name=_('Имя'),
        on_delete=models.SET_NULL,
        related_name='building',
        null=True,
        blank=True
    )
    phone = models.ForeignKey(
        Phone,
        verbose_name=_('Телефон'),
        on_delete=models.SET_NULL,
        related_name='building',
        null=True,
        blank=True
    )
    newbuilding = models.ForeignKey(
        NewBuilding,
        verbose_name=_('Новострои'),
        on_delete=models.SET_NULL,
        related_name='building',
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

    video = models.TextField(
        verbose_name=_('Код видео'),
        blank=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    period = models.CharField(
        verbose_name=_('Период'),
        choices=Period.CHOICES,
        max_length=50,
        blank=True,
        null=True
    )
    proposal = models.CharField(
        verbose_name=_('Предложение'),
        choices=Proposal.CHOICES,
        max_length=50,
        blank=True,
        null=True
    )
    images = GenericRelation(Photo, related_query_name='building')

    objects = BuildingManager()

    class Meta:
        verbose_name = _('Квартиры и Дома')
        verbose_name_plural = _('Квартиры и Дома')
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
        self.SEOKeywords = _(self.SEODescription)
        super(Building, self).save(*args, **kwargs)



    def get_edit_url(self):
        return reverse('admin2:building_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:building_delete', args=[self.id])

    def get_absolute_url(self):
        return reverse('objects:buildings_detail', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:buildings')

    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__).id

    def meta(self):
        return self._meta

    def normalize_SEO(self, text):
        if not text:
            return ''
        try:
            if settings.LANGUAGE_CODE == 'uk':
                text = text.replace('Будинок', 'будинку')
                text = text.replace('Квартира', 'квартири')
                text = text.replace('Кімната', 'кімнати')
            elif settings.LANGUAGE_CODE == 'ru':
                text = text.replace('Дом', 'дома')
                text = text.replace('Квартира', 'квартиры')
                text = text.replace('Комната', 'комнаты')
        except AttributeError:
            return text
        return text

    def get_title(self):
        appointment = self.normalize_SEO(self.get_appointment_display())
        return '{0} {1}'.format(self.get_type_deal_display() or '', appointment or '')

    def get_phuket_title(self):
        proposal = self.normalize_SEO(self.get_proposal_display())
        return '{0} {1}'.format(self.get_type_deal_display(), proposal)

    def footage_price(self):
        if self.footage and self.price:
            return self.price // self.footage

    def get_current(self):
        if self.type_deal == TypeDeal.SALE:
            return '$'
        elif self.type_deal == TypeDeal.RENT:
            return Settings.get_solo().get_currency_display()
