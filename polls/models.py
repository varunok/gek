# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField(
        verbose_name='Вопрос',
        max_length=200
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['id']

    def __unicode__(self):
        return self.question_text

    def get_edit_url(self):
        return reverse('admin2:edit_question', args=[self.id])

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    choice_text = models.CharField(verbose_name='Вариант',max_length=200)
    ball = models.IntegerField(verbose_name='Балл',default=0)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __unicode__(self):
        return self.choice_text


class Result(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250
    )
    description = RichTextUploadingField(
        verbose_name='Комментарий'
    )
    title_image = models.ImageField(
        verbose_name='Фото Заголовок',
        upload_to='result/%Y/%m/%d/',
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото Результат',
        upload_to='result/%Y/%m/%d/',
        blank=True
    )
    ball_from = models.IntegerField(
        verbose_name='Баллов От'
    )
    ball_to = models.IntegerField(
        verbose_name='Баллов До'
    )
    class Meta:
        verbose_name='Результат'
        verbose_name_plural='Результаты'

    def __unicode__(self):
        return self.title


class Polls(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=250
    )
    test_end = models.IntegerField(
        verbose_name='Тест прошло',
        default=0
    )
    questions = models.ManyToManyField(
        Question,
        verbose_name='Вопросы',
        related_name='polls'
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='polls/%Y/%m/%d/',
        blank=True
    )
    results = models.ManyToManyField(
        Result,
        verbose_name='Результаты',
        related_name='polls'
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name='Контент'
    )


    class Meta:
        verbose_name='Тест'
        verbose_name_plural='Тесты'

    def __unicode__(self):
        return self.title

    def get_edit_url(self):
        return reverse('admin2:poll_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('admin2:poll_delete', args=[self.id])

    def get_absolute_url(self):
        return reverse('polls:test_start', args=[self.id])






