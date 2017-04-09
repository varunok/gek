# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from solo.models import SingletonModel


class Settings(SingletonModel):
    UAH = 'UAH'
    RUB = 'RUB'
    KZT = 'KZT'
    CARRENCY = (
        (UAH, 'грн'),
        (RUB, 'руб'),
        (KZT, 'тнг')
    )
    currency = models.CharField(
        verbose_name='Валюта',
        choices=CARRENCY,
        max_length=3,
        blank=True
    )
    dollar_rate = models.FloatField(
        verbose_name='Курс доллара',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"





class IndexPageModel(SingletonModel):
    name = models.CharField(
        default='Главная',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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

    class Meta:
        verbose_name = 'Главная'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class NewBuildingPageModel(SingletonModel):
    name = models.CharField(
        default='Новострои',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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
    is_enable = models.BooleanField(
        verbose_name='Включена ли страница?',
        default=True
    )

    class Meta:
        verbose_name = 'Новострои'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class DailyPageModel(SingletonModel):
    name = models.CharField(
        default='Посуточна',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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
    is_enable = models.BooleanField(
        verbose_name='Включена ли страница?',
        default=True
    )

    class Meta:
        verbose_name = 'Посуточна'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class BuildingPageModel(SingletonModel):
    name = models.CharField(
        default='Квартиры и Дома',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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
    is_enable = models.BooleanField(
        verbose_name='Включена ли страница?',
        default=True
    )

    class Meta:
        verbose_name = 'Квартиры и Дома'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class OfisPageModel(SingletonModel):
    name = models.CharField(
        default='Офисы и магазины',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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
    is_enable = models.BooleanField(
        verbose_name='Включена ли страница?',
        default=True
    )

    class Meta:
        verbose_name = 'Офисы и магазины'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class TrustPageModel(SingletonModel):
    name = models.CharField(
        default='Доверее',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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

    class Meta:
        verbose_name = 'Доверее'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class ContactPageModel(SingletonModel):
    name = models.CharField(
        default='Доверее',
        verbose_name='Контакты',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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

    class Meta:
        verbose_name = 'Контакты'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')
