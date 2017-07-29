# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from datetime import date

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from solo.models import SingletonModel

from common.models import Photo, Video, FAQ, Feed, Schedule
from users.models import User

from django.utils.translation import ugettext_lazy as _


class CurrencyChoice(object):
    UAH = 'UAH'
    RUB = 'RUB'
    KZT = 'KZT'
    THB = 'THB'
    CARRENCY = (
        (UAH, 'грн'),
        (RUB, 'руб'),
        (KZT, 'тнг'),
        (THB, 'бат')
    )

class CurrencyPayChoice(object):
    UAH = 'UAH'
    RUB = 'RUB'
    USD = 'USD'
    CARRENCY = (
        (UAH, 'UAH'),
        (RUB, 'RUB'),
        (USD, 'USD')
    )


class HelpManager(models.Manager):
    def is_enable(self, *args, **kwargs):
        kwargs['is_enable'] = True
        return self.filter(*args, **kwargs)


class Help(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=500,
        blank=True,
        null=True
    )
    video = models.TextField(
        verbose_name=_('Код видео'),
        blank=True,
        null=True
    )
    is_enable = models.BooleanField(
        verbose_name=_('Включено?'),
        default=True
    )

    objects = HelpManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Видео')
        verbose_name = _('Видео')

    def get_edit_url(self):
        return reverse('admin2:help_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:help_delete', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:helps_list')


class Settings(SingletonModel):

    currency = models.CharField(
        verbose_name=_('Валюта'),
        choices=CurrencyChoice.CARRENCY,
        max_length=3,
        blank=True
    )
    dollar_rate = models.FloatField(
        verbose_name=_('Курс доллара'),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return _("Валюта")

    class Meta:
        verbose_name = "Валюта"


class SettingsAddress(SingletonModel):
    phone = models.CharField(
        verbose_name=_('Телефон'),
        max_length=50,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name=_('Город'),
        max_length=50,
        blank=True,
        null=True
    )
    city_plural = models.CharField(
        verbose_name=_('Город (родительный)'),
        max_length=50,
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name=_('Улица'),
        max_length=50,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=50,
        blank=True,
        null=True
    )


    def __unicode__(self):
        return _("Адреса")

    class Meta:
        verbose_name = _("Адреса")


def slug_validator(value):
    if False:
        raise ValidationError(
            '%(value)s уже используется.',
            params={'value': value},
        )


class SettingsFranchise(SingletonModel):
    price_30 = models.PositiveIntegerField(
        verbose_name=_('Стоимость 30 дней'),
        default=0
    )
    price_90 = models.PositiveIntegerField(
        verbose_name=_('Стоимость 90 дней'),
        default=0
    )
    price_180 = models.PositiveIntegerField(
        verbose_name=_('Стоимость 180 дней'),
        default=0
    )
    currency = models.CharField(
        verbose_name=_('Валюта'),
        choices=CurrencyPayChoice.CARRENCY,
        max_length=3,
        blank=True
    )

    class Meta:
        verbose_name = _('Стоимость франшизы')
        verbose_name_plural = _('Стоимость франшизы')


class SettingsPrivate24(SingletonModel):
    merchant = models.IntegerField(
        verbose_name=_('Приват24 merchant ID'),
        blank=True,
        null=True
    )
    signature = models.CharField(
        verbose_name=_('Приват24 signature'),
        blank=True,
        null=True,
        max_length=250
    )


class SettingsLiqpay(SingletonModel):
    merchant = models.CharField(
        verbose_name='Liqpay merchant ID',
        blank=True,
        null=True,
        max_length=250
    )
    signature = models.CharField(
        verbose_name='Liqpay signature',
        blank=True,
        null=True,
        max_length=250
    )


class ActiveFranchise(SingletonModel):
    active_franchise = models.DateField(
        verbose_name=_('Франшиза активна до'),
        default=timezone.now
    )

    def is_active(self):
        if self.active_franchise < date.today():
            return False
        else:
            return True


class EmailForward(models.Model):
    email = models.EmailField(
        verbose_name=_('Почта')
    )

    class Meta:
        verbose_name_plural = _('Почта для рассылки')
        verbose_name = _('Почта для рассылки')

    def __unicode__(self):
        return self.email

    def get_edit_url(self):
        return reverse('admin2:email_forward_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:email_forward_delete', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:email_forward')


class Counters(SingletonModel):
    counter_1 = models.TextField(
        verbose_name=_('Счетчик №1'),
        blank=True,
        null=True
    )
    counter_2 = models.TextField(
        verbose_name=_('Счетчик №2'),
        blank=True,
        null=True
    )
    counter_3 = models.TextField(
        verbose_name=_('Счетчик №3'),
        blank=True,
        null=True
    )
    counter_4 = models.TextField(
        verbose_name=_('Счетчик №4'),
        blank=True,
        null=True
    )


class IndexPageModel(SingletonModel):
    name = models.CharField(
        default=_('Главная'),
        verbose_name=_('Название'),
        max_length=30,
        unique=True,
        editable=False
    )
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify(_('Главная'), allow_unicode=True),
        validators=[slug_validator],
        editable=False
    )
    title_seo = models.TextField(
        verbose_name=_('Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )
    video = models.TextField(
        verbose_name=_('Код видео'),
        blank=True
    )

    class Meta:
        verbose_name = _('Главная')

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')


class NewBuildingPageModel(SingletonModel):
    name = models.CharField(
        default=_('Новострои'),
        verbose_name=_('Название'),
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
    title_seo = models.TextField(
        verbose_name=_('Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Включена ли страница?'),
        default=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )

    class Meta:
        verbose_name = 'Новострои'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('objects:newbuildings')


class DailyPageModel(SingletonModel):
    name = models.CharField(
        default=_('Посуточна'),
        verbose_name=_('Название'),
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
    title_seo = models.TextField(
        verbose_name=_('Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Включена ли страница?'),
        default=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )

    class Meta:
        verbose_name = 'Посуточна'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('objects:dailys')


class BuildingPageModel(SingletonModel):
    name = models.CharField(
        default=_('Квартиры и Дома'),
        verbose_name=_('Название'),
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
    title_seo = models.TextField(
        verbose_name=_('SEO Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Включена ли страница?'),
        default=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )

    class Meta:
        verbose_name = 'Квартиры и Дома'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('objects:buildings')


class EarthPageModel(SingletonModel):
    name = models.CharField(
        default=_('Земля'),
        verbose_name=_('Название'),
        max_length=30,
        unique=True,
        editable=False
    )
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Земля', allow_unicode=True),
        validators=[slug_validator],
        editable=False
    )
    title_seo = models.TextField(
        verbose_name=_('SEO Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Включена ли страница?'),
        default=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )

    class Meta:
        verbose_name = 'Земля'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('objects:earth')


class OfisPageModel(SingletonModel):
    name = models.CharField(
        default=_('Офисы и магазины'),
        verbose_name=_('Название'),
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
    title_seo = models.TextField(
        verbose_name=_('Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Включена ли страница?'),
        default=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )

    class Meta:
        verbose_name = 'Офисы и магазины'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('objects:ofices')


class TrustPageModel(SingletonModel):
    name = models.CharField(
        default=_('Доверее'),
        verbose_name=_('Название'),
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
    title_seo = models.TextField(
        verbose_name=_('Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    video = models.TextField(
        verbose_name=_('Код видео'),
        blank=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )
    faq_enable = models.BooleanField(
        verbose_name=_('Влючен ли FAQ?'),
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
        return reverse('trust:trust')


class ContactPageModel(SingletonModel):
    name = models.CharField(
        default=_('Контакты'),
        verbose_name=_('Название'),
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
    title_seo = models.TextField(
        verbose_name=_('Заголовок'),
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name=_('Подзаголовок'),
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
        verbose_name=_('Фото'),
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    image_seo = models.ImageField(
        verbose_name=_('Фото SEO'),
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )
    title = models.TextField(
        verbose_name=_('Заголовок H1'),
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    our_address = models.CharField(
        verbose_name=_('Наш адрес'),
        max_length=250,
        blank=True,
        null=True
    )
    our_email = models.EmailField(
        verbose_name='E-mail',
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name=_('Телефон'),
        max_length=100,
        blank=True,
        null=True
    )
    schedules = GenericRelation(Schedule, related_query_name='contact')
    users = models.ManyToManyField(User,
                                   related_name='contact',
                                   blank=True,
                                   verbose_name=_('Наши специалисты'))

    class Meta:
        verbose_name = 'Контакты'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('contacts:contact')


class Notes(models.Model):
    note = models.TextField(
        verbose_name='Задача'
    )
    date_do = models.DateTimeField(
        verbose_name='До какого числа?',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['date_do']

    def __unicode__(self):
        return '{0}... до {1}'.format(self.note if len(self.note)<10 else self.note[:11], self.date_do)

    def get_delete_url(self):
        return reverse('admin2:notes_delete', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:notes')
