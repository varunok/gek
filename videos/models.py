# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

# Create your models here.
from django.urls import reverse

from common.models import WhatYouKnown


class Videos(models.Model):
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
        verbose_name='Заголовок',
        blank=True
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
    time = models.TimeField(
        verbose_name='Время',
        blank=True,
        null=True,
        help_text='формат 00:11:22'
    )
    views = models.IntegerField(
        verbose_name='Просмотры',
        default=0
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
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
    what_you_knowns = GenericRelation(WhatYouKnown, related_query_name='videos')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['-when_create']

    def __unicode__(self):
        if self.title:
            return self.title
        return '{0}'.format(self.id)

    def save(self, *args, **kwargs):
        if self.title:
            if not self.SEOTitle:
                self.SEOTitle = self.title
            if not self.SEOKeywords:
                self.SEOKeywords = self.title
            if not self.SEODescription:
                self.SEODescription = '{0}'.format(self.title)
        super(Videos, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('admin2:videos_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:videos_delete', args=[self.id])

    def get_absolute_url(self):
        return reverse('videos:videos_detail', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:videos')

    def meta(self):
        return self._meta
