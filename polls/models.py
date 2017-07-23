# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(
        verbose_name=_('Вопрос'),
        max_length=200
    )

    class Meta:
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')
        ordering = ['id']

    def __unicode__(self):
        return self.question_text

    def get_edit_url(self):
        return reverse('admin2:edit_question', args=[self.id])

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    choice_text = models.CharField(verbose_name=_('Вариант'),max_length=200)
    ball = models.IntegerField(verbose_name=_('Балл'),default=0)

    class Meta:
        verbose_name = _('Вариант')
        verbose_name_plural = _('Варианты')

    def __unicode__(self):
        return self.choice_text


class Result(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=250
    )
    description = RichTextUploadingField(
        verbose_name=_('Комментарий')
    )
    title_image = models.ImageField(
        verbose_name=_('Фото Заголовок'),
        upload_to='result/%Y/%m/%d/',
        blank=True
    )
    image = models.ImageField(
        verbose_name=_('Фото Результат'),
        upload_to='result/%Y/%m/%d/',
        blank=True
    )
    ball_from = models.IntegerField(
        verbose_name=_('Баллов От')
    )
    ball_to = models.IntegerField(
        verbose_name=_('Баллов До')
    )
    class Meta:
        verbose_name = _('Результат')
        verbose_name_plural = _('Результаты')

    def __unicode__(self):
        return self.title


class URLResult(models.Model):
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        allow_unicode=True
    )
    result = models.ForeignKey(
        Result,
        on_delete=models.PROTECT
    )
    ball = models.IntegerField(
        verbose_name=_('Результат')
    )

    class Meta:
        verbose_name='Тест'
        verbose_name_plural='Тесты'

    def __unicode__(self):
        return '{0} => {1}'.format(self.slug, self.result)

    def get_absolute_url(self):
        return reverse('polls:url_result', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(get_random_string(length=8), allow_unicode=True)
        super(URLResult, self).save(*args, **kwargs)


class Polls(models.Model):
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=250
    )
    test_end = models.IntegerField(
        verbose_name=_('Тест прошло'),
        default=0
    )
    questions = models.ManyToManyField(
        Question,
        verbose_name=_('Вопросы'),
        related_name='polls'
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='polls/%Y/%m/%d/',
        blank=True
    )
    results = models.ManyToManyField(
        Result,
        verbose_name=_('Результаты'),
        related_name='polls'
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name=_('Контент')
    )


    class Meta:
        verbose_name = _('Тест')
        verbose_name_plural = _('Тесты')

    def __unicode__(self):
        return self.title

    def get_edit_url(self):
        return reverse('admin2:poll_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:poll_delete', args=[self.id])

    def get_absolute_url(self):
        return reverse('polls:test_start', args=[self.id])






