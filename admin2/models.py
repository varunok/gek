# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from solo.models import SingletonModel

from common.models import Photo, Video, FAQ, Feed, Schedule


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


def slug_validator(value):
    if False:
        raise ValidationError(
            '%(value)s уже используется.',
            params={'value': value},
        )



class IndexPageModel(SingletonModel):
    name = models.CharField(
        default='Главная',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Главная', allow_unicode=True),
        validators=[slug_validator],
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
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Новострои', allow_unicode=True),
        validators=[slug_validator],
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
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Посуточна', allow_unicode=True),
        validators=[slug_validator],
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
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Квартиры и Дома', allow_unicode=True),
        validators=[slug_validator],
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
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Офисы и магазины', allow_unicode=True),
        validators=[slug_validator],
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
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Доверее', allow_unicode=True),
        validators=[slug_validator],
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    video = models.TextField(
        verbose_name='Код видео',
        blank=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    faq_enable = models.BooleanField(
        verbose_name='Влючен ли FAQ?',
        default=True
    )
    images = GenericRelation(Photo, related_query_name='trust')
    videos = GenericRelation(Video, related_query_name='trust')
    fag = GenericRelation(FAQ, related_query_name='trust')
    feeds = GenericRelation(Feed, related_query_name='trust')

    class Meta:
        verbose_name = 'Доверее'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class ContactPageModel(SingletonModel):
    name = models.CharField(
        default='Контакты',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Контакты', allow_unicode=True),
        validators=[slug_validator],
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    our_address = models.CharField(
        verbose_name='Наш адрес',
        max_length=250,
        blank=True,
        null=True
    )
    our_email = models.EmailField(
        verbose_name='E-mail',
        blank=True,
        null=True
    )
    schedules = GenericRelation(Schedule, related_query_name='contact')

    class Meta:
        verbose_name = 'Контакты'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')
