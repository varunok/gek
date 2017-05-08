# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from multiselectfield import MultiSelectField

from rieltor_object.models import District


class TypeDeal(object):
    RENT = 'rent'
    SALE = 'sale'
    RENT_SALE = 'rent_sale'
    CHOICES = (
        (RENT, 'Аренда'),
        (SALE, 'Продажа'),
        (RENT_SALE, 'Аренда/Продажа')
    )

class TypeAppointment(object):
    APARTMENT = 'apartment'
    HOUSE = 'house'
    OFFICE = 'office'
    SHOP = 'shop'
    CHOICES = (
        (APARTMENT, 'Квартира'),
        (HOUSE, 'Дом'),
        (OFFICE, 'Офис'),
        (SHOP, 'Магазин')
    )


class Landing(models.Model):
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        blank=True,
        null=True,
        allow_unicode=True
    )
    type_deal = models.CharField(
        verbose_name='Аренда \ продажа',
        choices=TypeDeal.CHOICES,
        max_length=50,
    )
    type_property = MultiSelectField(
        verbose_name='Тип недвижимости',
        max_length=50,
        choices=TypeAppointment.CHOICES,
        blank=True,
        null=True
    )
    price_gt = models.IntegerField(
        verbose_name='Цена от',
        blank=True,
        null=True
    )
    price_lt = models.IntegerField(
        verbose_name='Цена до',
        blank=True,
        null=True
    )
    footage_gt = models.IntegerField(
        verbose_name='Площадь от',
        blank=True,
        null=True
    )
    footage_lt = models.IntegerField(
        verbose_name='Площадь до',
        blank=True,
        null=True
    )
    rooms = models.IntegerField(
        verbose_name='Комнат',
        blank=True,
        null=True
    )
    district = models.ForeignKey(
        District,
        verbose_name='Район',
        on_delete=models.SET_NULL,
        related_name='landing',
        null=True,
        blank=True
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
    title = models.TextField(
        verbose_name='SEO Заголовок',
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name='Контент SEO'
    )
    image_seo = models.ImageField(
        verbose_name='Фото SEO',
        upload_to='landing/%Y/%m/%d/',
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='landing/%Y/%m/%d/',
        blank=True
    )
    title_footer = models.CharField(
        verbose_name='Название для футера',
        max_length=200,
        blank=True,
        null=True
    )
    title_h1 = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
    )
    title_form = models.CharField(
        verbose_name='Заголовок форма',
        max_length=200,
        blank=True,
        null=True
    )
    subtitle_form = models.CharField(
        verbose_name='Подзаголовок форма',
        max_length=200,
        blank=True,
        null=True
    )
    image_form = models.ImageField(
        verbose_name='Фото форма',
        upload_to='landing/%Y/%m/%d/',
        blank=True
    )

    class Meta:
        verbose_name = 'Мультилендинг'
        verbose_name_plural = 'Мультилендинги'

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('landings:landing', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:landing_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:landing_delete', args=[self.id])
