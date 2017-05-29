# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from solo.models import SingletonModel

from common.models import Video, FAQ, Photo, TableRepair, BasePacket, MidlePacket, ExpertPacket, Advantage


class Partner(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=500,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='Email',
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name='Телефон',
        blank=True,
        null=True,
        max_length=250
    )
    is_phone_confirmed = models.BooleanField(
        verbose_name='Телефон подтвержден?',
        default=False
    )
    comment = models.TextField(
        verbose_name='Коментарий',
        blank=True
    )
    application_count = models.IntegerField(
        verbose_name='Число заявок',
        default=0
    )
    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        # limit_choices_to={'model__in': somsing}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.name if self.name else self.id)


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
        verbose_name='Фото аватар',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    image_avatar = models.ImageField(
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
    description = models.TextField(
        verbose_name='Описание главная услуги',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        blank=True,
        null=True,
        default='Услуги риелторские'
    )
    videos = GenericRelation(Video, related_query_name='services_rieltor')
    fag = GenericRelation(FAQ, related_query_name='services_rieltor')
    partners = GenericRelation(Partner, related_query_name='services_rieltor')

    class Meta:
        verbose_name = 'Услуги риелторские'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:rieltor_service', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:rieltor_service_edit')


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
        verbose_name='Фото аватар',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    image_avatar = models.ImageField(
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
    description = models.TextField(
        verbose_name='Описание главная услуги',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        blank=True,
        null=True,
        default='Оценка недвижимости'
    )
    videos = GenericRelation(Video, related_query_name='valuation')
    fag = GenericRelation(FAQ, related_query_name='valuation')
    partners = GenericRelation(Partner, related_query_name='valuation')

    class Meta:
        verbose_name = 'Оценка недвижимости'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:valuation', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:valuation_edit')


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
        verbose_name='Фото аватар',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    image_avatar = models.ImageField(
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
    description = models.TextField(
        verbose_name='Описание главная услуги',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        blank=True,
        null=True,
        default='Ремонт помещения'
    )
    videos = GenericRelation(Video, related_query_name='repair')
    repairs = GenericRelation(TableRepair, related_query_name='repair')
    images = GenericRelation(Photo, related_query_name='repair')
    partners = GenericRelation(Partner, related_query_name='repair')

    class Meta:
        verbose_name = 'Ремонт помещения'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:repair', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:repair_edit')


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
        verbose_name='Фото аватар',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    image_avatar = models.ImageField(
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
    description = models.TextField(
        verbose_name='Описание главная услуги',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        blank=True,
        null=True,
        default='Страхование недвижимости'
    )
    videos = GenericRelation(Video, related_query_name='insurance')
    images = GenericRelation(Photo, related_query_name='insurance')
    fag = GenericRelation(FAQ, related_query_name='insurance')
    partners = GenericRelation(Partner, related_query_name='insurance')

    class Meta:
        verbose_name = 'Страхование недвижимости'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:insurance', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:insurence_edit')


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
        verbose_name='Фото аватар',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    image_avatar = models.ImageField(
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
    description = models.TextField(
        verbose_name='Описание главная услуги',
        blank=True,
        null=True
    )
    videos = GenericRelation(Video, related_query_name='cleaning')
    images = GenericRelation(Photo, related_query_name='cleaning')
    partners = GenericRelation(Partner, related_query_name='cleaning')
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
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        blank=True,
        null=True,
        default='Уборка квартир'
    )

    class Meta:
        verbose_name = 'Уборка квартир'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:cleaning', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:cleaning_edit')


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
        verbose_name='Фото аватар',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    image_avatar = models.ImageField(
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
    description = models.TextField(
        verbose_name='Описание главная услуги',
        blank=True,
        null=True
    )
    videos = GenericRelation(Video, related_query_name='installation_water')
    images = GenericRelation(Photo, related_query_name='installation_water')
    fag = GenericRelation(FAQ, related_query_name='installation_water')
    partners = GenericRelation(Partner, related_query_name='installation_water')
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
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        blank=True,
        null=True,
        default='Установка водомера'
    )

    class Meta:
        verbose_name = 'Установка водомера'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:installation_water', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:installation_water_edit')



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
        verbose_name='Фото аватар',
        upload_to='services/%Y/%m/%d/',
        blank=True
    )
    image_avatar = models.ImageField(
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
    description = models.TextField(
        verbose_name='Описание главная услуги',
        blank=True,
        null=True
    )
    videos = GenericRelation(Video, related_query_name='universal')
    images = GenericRelation(Photo, related_query_name='universal')
    fag = GenericRelation(FAQ, related_query_name='universal')
    advantages = GenericRelation(Advantage, related_query_name='universal')
    partners = GenericRelation(Partner, related_query_name='universal')
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

    def get_delete_url(self):
        return reverse('admin2:universal_delete', args=[self.id])

    def get_edit_url(self):
        return reverse('admin2:universal_edit', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:services')

