# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from multiselectfield import MultiSelectField

from common.models import Photo
from rieltor_object.models.common_objects import *


class Earth(models.Model):
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
    contact_name = models.CharField(
        verbose_name='Контактное лицо',
        max_length=250,
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=250,
        blank=True,
        null=True
    )
    description = models.TextField(
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
    images = GenericRelation(Photo, related_query_name='earth')

    class Meta:
        verbose_name = 'Земля'
        verbose_name_plural = 'Земля'
        ordering = ['-when_create']

    def __unicode__(self):
        return '{0}'.format(self.id)

    def save(self, *args, **kwargs):
        if self.title:
            if not self.SEOTitle:
                self.SEOTitle = self.title
            if not self.SEOKeywords:
                self.SEOKeywords = self.title
            if not self.SEODescription:
                self.SEODescription = '{0} {1} {2}'.format(self.address, self.price,
                                                           self.title)
        super(Earth, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('admin2:earth_edit', args=[self.id])

    # def get_absolute_url(self):
    #     return reverse('objects:earth_detail', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:earth')

    def meta(self):
        return self._meta
