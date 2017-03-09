# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Application(models.Model):
    HOME = 'home'
    CHOICES_SOURCE = (
        (HOME, 'Главная'),
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    source = models.CharField(
        choices=CHOICES_SOURCE,
        verbose_name='Источник',
        max_length=150
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=50,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=200,
        blank=True,
        null=True
    )
    text = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return '%s' % (self.id)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created']
