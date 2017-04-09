# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from solo.models import SingletonModel

from common.models import Video, FAQ, Photo, TableRepair, BasePacket, MidlePacket, ExpertPacket, Advantage


def slug_validator(value):
    if False:
        raise ValidationError(
            '%(value)s уже используется.',
            params={'value': value},
        )


class ServicesRieltor(SingletonModel):
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Услуги риелторские', allow_unicode=True),
        validators=[slug_validator]
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    is_enable = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    faq_enable = models.BooleanField(
        verbose_name='Влючен ли FAQ?',
        default=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    videos = GenericRelation(Video, related_query_name='services_rieltor')
    fag = GenericRelation(FAQ, related_query_name='services_rieltor')

    class Meta:
        verbose_name = 'Услуги риелторские'

    def __unicode__(self):
        return 'Услуги риелторские'

    def get_absolute_url(self):
        return reverse('services:rieltor_service', args=[self.slug])


class Valuation(SingletonModel):
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Оценка недвижимости', allow_unicode=True),
        validators=[slug_validator]
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    is_enable = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    faq_enable = models.BooleanField(
        verbose_name='Влючен ли FAQ?',
        default=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    videos = GenericRelation(Video, related_query_name='valuation')
    fag = GenericRelation(FAQ, related_query_name='valuation')

    class Meta:
        verbose_name = 'Оценка недвижимости'

    def __unicode__(self):
        return 'Оценка недвижимости'

    def get_absolute_url(self):
        return reverse('services:valuation', args=[self.slug])


class Repair(SingletonModel):
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Ремонт помещения', allow_unicode=True),
        validators=[slug_validator]
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
        blank=True,
        null=True
    )
    subtitle = models.CharField(
        verbose_name='Подзаголовок',
        max_length=250,
        blank=True,
        null=True
    )
    help_subtitle = models.CharField(
        verbose_name='Под-под-заголовок',
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    is_enable = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    faq_enable = models.BooleanField(
        verbose_name='Влючен ли FAQ?',
        default=True
    )
    image_enable = models.BooleanField(
        verbose_name='Влючени ли фото?',
        default=True
    )
    repairs_enable = models.BooleanField(
        verbose_name='Влючена ли Стоимость ремонта?',
        default=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    videos = GenericRelation(Video, related_query_name='repair')
    repairs = GenericRelation(TableRepair, related_query_name='repair')
    images = GenericRelation(Photo, related_query_name='repair')

    class Meta:
        verbose_name = 'Ремонт помещения'

    def __unicode__(self):
        return 'Ремонт помещения'

    def get_absolute_url(self):
        return reverse('services:repair', args=[self.slug])


class Insurance(SingletonModel):
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Страхование недвижимости', allow_unicode=True),
        validators=[slug_validator]
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    is_enable = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    faq_enable = models.BooleanField(
        verbose_name='Влючен ли FAQ?',
        default=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    videos = GenericRelation(Video, related_query_name='insurance')
    images = GenericRelation(Photo, related_query_name='insurance')
    fag = GenericRelation(FAQ, related_query_name='insurance')

    class Meta:
        verbose_name = 'Страхование недвижимости'

    def __unicode__(self):
        return 'Страхование недвижимости'

    def get_absolute_url(self):
        return reverse('services:insurance', args=[self.slug])


class Cleaning(SingletonModel):
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Уборка квартир', allow_unicode=True),
        validators=[slug_validator]
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    is_enable = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    packet_enable = models.BooleanField(
        verbose_name='Влючен ли пакет?',
        default=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    videos = GenericRelation(Video, related_query_name='cleaning')
    images = GenericRelation(Photo, related_query_name='cleaning')
    base_packet = models.OneToOneField(
        BasePacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет начинающий',
        related_query_name='cleaning',
        blank=True,
        null=True
    )
    midle_packet = models.OneToOneField(
        MidlePacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет Продвинутый',
        related_query_name='cleaning',
        blank=True,
        null=True
    )
    expert_packet = models.OneToOneField(
        ExpertPacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет Эксперт',
        related_query_name='cleaning',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Уборка квартир'

    def __unicode__(self):
        return 'Уборка квартир'

    def get_absolute_url(self):
        return reverse('services:cleaning', args=[self.slug])


class InstallationWater(SingletonModel):
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        default=slugify('Установка водомера', allow_unicode=True),
        validators=[slug_validator]
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
        blank=True,
        null=True
    )
    subtitle = models.CharField(
        verbose_name='Подзаголовок',
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    is_enable = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    packet_enable = models.BooleanField(
        verbose_name='Влючен ли пакет?',
        default=True
    )
    faq_enable = models.BooleanField(
        verbose_name='Влючен ли FAQ?',
        default=True
    )
    videos = GenericRelation(Video, related_query_name='installation_water')
    images = GenericRelation(Photo, related_query_name='installation_water')
    fag = GenericRelation(FAQ, related_query_name='installation_water')
    base_packet = models.OneToOneField(
        BasePacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет начинающий',
        related_query_name='installation_water',
        blank=True,
        null=True
    )
    midle_packet = models.OneToOneField(
        MidlePacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет Продвинутый',
        related_query_name='installation_water',
        blank=True,
        null=True
    )
    expert_packet = models.OneToOneField(
        ExpertPacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет Эксперт',
        related_query_name='installation_water',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Установка водомера'

    def __unicode__(self):
        return 'Установка водомера'

    def get_absolute_url(self):
        return reverse('services:installation_water', args=[self.slug])


class UniversalService(models.Model):
    slug = models.SlugField(
        verbose_name='URL',
        allow_unicode=True,
        validators=[slug_validator],
        unique=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        unique=True
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    is_enable = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    packet_enable = models.BooleanField(
        verbose_name='Влючен ли пакет?',
        default=True
    )
    faq_enable = models.BooleanField(
        verbose_name='Влючен ли FAQ?',
        default=True
    )
    videos = GenericRelation(Video, related_query_name='universal')
    images = GenericRelation(Photo, related_query_name='universal')
    fag = GenericRelation(FAQ, related_query_name='universal')
    advantages = GenericRelation(Advantage, related_query_name='universal')
    base_packet = models.OneToOneField(
        BasePacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет начинающий',
        related_query_name='universal',
        blank=True,
        null=True
    )
    midle_packet = models.OneToOneField(
        MidlePacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет Продвинутый',
        related_query_name='universal',
        blank=True,
        null=True
    )
    expert_packet = models.OneToOneField(
        ExpertPacket,
        on_delete=models.SET_NULL,
        verbose_name='Пакет Эксперт',
        related_query_name='installation_water',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Универсальная услуга"
        verbose_name_plural = "Универсальние услуги"
        ordering = ['id']

    def __unicode__(self):
        return '{0} - {1}'.format(self.name, self.slug)

    def get_absolute_url(self):
        return reverse('services:universal', args=[self.slug])

