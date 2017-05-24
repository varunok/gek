# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from multiselectfield import MultiSelectField

from admin2.models import SettingsAddress
from common.models import Photo
from rieltor_object.models.common_objects import *


class Earth(models.Model):
    custom_id = models.PositiveIntegerField(
        verbose_name='ID',
        unique=True,
        blank=True,
        null=True
    )
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
    district = models.ForeignKey(
        EarthDistrict,
        verbose_name='Район',
        on_delete=models.SET_NULL,
        related_name='earth',
        null=True,
        blank=True
    )
    type_area = models.CharField(
        verbose_name='Тип Участка',
        max_length=50,
        choices=TypeArea.CHOICES,
        blank=True,
        null=True
    )
    to_city = models.IntegerField(
        verbose_name='До города, км',
        blank=True,
        null=True
    )
    communication = MultiSelectField(
        verbose_name='Коммуникации',
        max_length=50,
        choices=Communications.CHOICES,
        blank=True,
        null=True
    )
    structure_house = MultiSelectField(
        verbose_name='Строение дома',
        max_length=50,
        choices=StructureHouse.CHOICES,
        blank=True,
        null=True
    )
    area = models.IntegerField(
        verbose_name='Площадь',
        blank=True,
        null=True
    )
    description = RichTextUploadingField(
        verbose_name='Описание',
        blank=True
    )
    geo = models.TextField(
        verbose_name='На карте',
        blank=True
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
    name = models.ForeignKey(
        Name,
        verbose_name='Имя',
        on_delete=models.SET_NULL,
        related_name='earth',
        null=True,
        blank=True
    )
    phone = models.ForeignKey(
        Phone,
        verbose_name='Телефон',
        on_delete=models.SET_NULL,
        related_name='earth',
        null=True,
        blank=True
    )
    images = GenericRelation(Photo, related_query_name='earth')

    class Meta:
        verbose_name = 'Земля'
        verbose_name_plural = 'Земля'
        ordering = ['-when_create']

    def __unicode__(self):
        if self.SEODescription:
            return '{0}'.format(self.SEODescription)
        return '{0}'.format(self.id)

    def save(self, *args, **kwargs):
        self.SEOTitle = self.normalize_SEO('Участок {0} по {1} район {2} ценна {3} в {4}'.format(
            self.get_type_area_display() or '',
            self.address or '',
            self.district or '',
            self.price or '',
            SettingsAddress.get_solo().city_plural or ''))
        self.SEODescription = self.normalize_SEO('Участок {0}  в новострое по {1} район {2} в {3}'.format(
            self.get_type_area_display() or '',
            self.address or '',
            self.district or '',
            SettingsAddress.get_solo().city_plural or ''))
        self.SEOKeywords = self.SEODescription
        super(Earth, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('admin2:earth_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:earth_delete', args=[self.id])

    # def get_absolute_url(self):
    #     return reverse('objects:earth_detail', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:earth')

    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__).id

    def meta(self):
        return self._meta

    def normalize_SEO(self, text):
        return text
