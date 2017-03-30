# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from solo.models import SingletonModel

from common.models import Video, FAQ


class ServicesRieltor(SingletonModel):
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
    is_active = models.BooleanField(
        verbose_name='Влючен ли?',
        default=True
    )
    videos = GenericRelation(Video, related_query_name='services_rieltor')
    fag = GenericRelation(FAQ, related_query_name='services_rieltor')

    class Meta:
        verbose_name = 'Услуги риелторские'

    def __unicode__(self):
        return 'Услуги риелторские'

