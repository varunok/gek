# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from multiselectfield import MultiSelectField

from rieltor_object.models import District

from django.utils.translation import ugettext_lazy as _


class TypeDeal(object):
    RENT = 'rent'
    SALE = 'sale'
    # RENT_SALE = 'rent_sale'
    CHOICES = (
        (RENT, _('Аренда')),
        (SALE, _('Продажа')),
        # (RENT_SALE, 'Аренда/Продажа')
    )

class TypeAppointment(object):
    APARTMENT = 'apartment'
    HOUSE = 'house'
    OFFICE = 'office'
    SHOP = 'shop'
    CHOICES = (
        (APARTMENT, _('Квартира')),
        (HOUSE, _('Дом')),
        (OFFICE, _('Офис')),
        (SHOP, _('Магазин'))
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
        verbose_name=_('Аренда \ продажа'),
        choices=TypeDeal.CHOICES,
        max_length=50,
    )
    type_property = MultiSelectField(
        verbose_name=_('Тип недвижимости'),
        max_length=50,
        choices=TypeAppointment.CHOICES,
        blank=True,
        null=True
    )
    price_gt = models.IntegerField(
        verbose_name=_('Цена от'),
        blank=True,
        null=True
    )
    price_lt = models.IntegerField(
        verbose_name=_('Цена до'),
        blank=True,
        null=True
    )
    footage_gt = models.IntegerField(
        verbose_name=_('Площадь от'),
        blank=True,
        null=True
    )
    footage_lt = models.IntegerField(
        verbose_name=_('Площадь до'),
        blank=True,
        null=True
    )
    rooms = models.IntegerField(
        verbose_name=_('Комнат'),
        blank=True,
        null=True
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('Район'),
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
    title_seo = models.TextField(
        verbose_name=_('SEO Заголовок'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент SEO')
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='landing/%Y/%m/%d/',
        blank=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='landing/%Y/%m/%d/',
        blank=True
    )
    title_footer = models.CharField(
        verbose_name=_('Название для футера'),
        max_length=200,
        blank=True,
        null=True
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=250,
    )
    title_form = models.CharField(
        verbose_name=_('Заголовок форма'),
        max_length=200,
        blank=True,
        null=True
    )
    subtitle_form = models.CharField(
        verbose_name=_('Подзаголовок форма'),
        max_length=200,
        blank=True,
        null=True
    )
    image_form = models.ImageField(
        verbose_name=_('Фото форма'),
        upload_to='landing/%Y/%m/%d/',
        blank=True
    )

    class Meta:
        verbose_name = _('Мультилендинг')
        verbose_name_plural = _('Мультилендинги')

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('landings:landing', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:landing_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:landing_delete', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:landings')


class LandingFutor(models.Model):
    landing = models.OneToOneField(
        Landing,
        related_name='landing_futor',

    )

    def __unicode__(self):
        return self.landing.title

    def get_delete_url(self):
        return reverse('admin2:landing_futor_delete', args=[self.id])
