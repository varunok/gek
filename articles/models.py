# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


class Sections(models.Model):
    name = models.CharField(
        verbose_name='Навзвание',
        max_length=150
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        blank=True,
        null=True,
        allow_unicode=True
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=150
    )
    keywords = models.TextField(
        verbose_name='Keywords',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    heading = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

    def __unicode__(self):
        if self.slug:
            return self.slug
        else:
            return '%s' % self.id

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('admin2:detail', args=[self.slug]) #TODO Змінити url на article коли буде верстка

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Sections, self).save(*args, **kwargs)


