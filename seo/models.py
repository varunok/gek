# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse


class SEO(models.Model):
    title = models.TextField(
        verbose_name='Заголовок',
    )
    title_h1 = models.TextField(
        verbose_name='Заголовок H1',
        blank=True,
        null=True
    )
    url = models.URLField(
        verbose_name='URL',
        unique=True,
        help_text='Полний путь. Пример http://example.com'
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name='Контент'
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
        upload_to='seo/%Y/%m/%d/',
        blank=True
    )

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

    def __unicode__(self):
        return self.title

    def get_delete_url(self):
        return reverse('admin2:seo_delete', args=[self.id])

    def get_edit_url(self):
        return reverse('admin2:seo_edit', args=[self.id])

    def get_list_url(self):
        return reverse('admin2:seo')
