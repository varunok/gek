# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.urls import reverse


class Sections(models.Model):
    name = models.CharField(
        verbose_name='Название',
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
    content = RichTextUploadingField(
        blank=True,
        verbose_name='Контент'
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = 'id',

    def __unicode__(self):
        if self.slug:
            return self.slug
        else:
            return '%s' % self.id

    def get_absolute_url(self):
        return reverse('articles:sections_detail', args=[self.slug])

    def get_delete_url(self):
        return reverse('admin2:sections_delete', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:sections_update', args=[self.slug])

    def get_list_url(self):
        return reverse('admin2:sections')

    def save(self, *args, **kwargs):
        if not self.slug and not Sections.objects.filter(slug=self.title).exists():
            self.slug = slugify(self.title, allow_unicode=True)
        elif not self.slug and not Sections.objects.filter(slug=self.name).exists():
            self.slug = slugify(self.name, allow_unicode=True)
        elif not self.slug and not self.title and not self.name:
            self.slug = slugify(get_random_string(length=8), allow_unicode=True)
        super(Sections, self).save(*args, **kwargs)


class Articles(models.Model):
    sections = models.ForeignKey(
        Sections,
        verbose_name='Рубрика',
        on_delete=models.CASCADE,
        related_name='articles'
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
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
    content = RichTextUploadingField(
        blank=True,
        verbose_name='Контент'
    )
    video = models.TextField(
        verbose_name='Код видео',
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='articles/%Y/%m/%d/',
        blank=True
    )
    views = models.IntegerField(
        verbose_name='Просмотры',
        default=0
    )

    def __unicode__(self):
        if self.slug:
            return self.slug
        else:
            return '%s' % self.id

    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[self.sections.slug, self.slug])

    def get_delete_url(self):
        return reverse('admin2:articles_delete', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin2:articles_update', args=[self.slug])

    def get_list_url(self):
        return reverse('admin2:articles')

    def save(self, *args, **kwargs):
        if not self.slug and not Articles.objects.filter(slug=self.title).exists():
            self.slug = slugify(self.title, allow_unicode=True)
        elif not self.slug and not Articles.objects.filter(slug=self.heading).exists():
            self.slug = slugify(self.heading, allow_unicode=True)
        elif not self.slug and not self.title and not self.heading:
            self.slug = slugify(get_random_string(length=8), allow_unicode=True)
        super(Articles, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = '-id',