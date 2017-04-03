# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from solo.models import SingletonModel

from common.models import Video, FAQ


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

