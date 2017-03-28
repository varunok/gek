# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from solo.models import SingletonModel


class Settings(SingletonModel):
    UAH = 'UAH'
    RUB = 'RUB'
    KZT = 'KZT'
    CARRENCY = (
        (UAH, 'грн'),
        (RUB, 'руб'),
        (KZT, 'тнг')
    )
    currency = models.CharField(
        verbose_name='Валюта',
        choices=CARRENCY,
        max_length=3,
        blank=True
    )
    dollar_rate = models.FloatField(
        verbose_name='Курс доллара',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


class StaticPageModel(models.Model):

    class StaticName:
        INDEX = 'Главная'
        NEWBUILD = 'Новострои'
        DAILY = 'Посуточна'
        HOMES = 'Квартиры и Дома'
        SHOPS = 'Офисы и магазины'
        TRUST = 'Доверее'
        CONTACT = 'Контакты'

        CHOICES = (
            (INDEX, 'Главная'),
            (NEWBUILD, 'Новострои'),
            (DAILY, 'Посуточна'),
            (HOMES, 'Квартиры и Дома'),
            (SHOPS, 'Офисы и магазины'),
            (TRUST, 'Доверее'),
            (CONTACT, 'Контакты'),
        )

    name = models.CharField(
        choices=StaticName.CHOICES,
        verbose_name='Название',
        max_length=30,
        unique=True
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    subtitle = models.TextField(
        verbose_name='Подзаголовок',
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
    is_enable = models.BooleanField(
        verbose_name='Включен ли?',
        default=True
    )

    class Meta:
        verbose_name = 'Статическая страница'
        verbose_name_plural = 'Статические страници'
        ordering = ('name',)

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        if self.name == 'Главная':
            return reverse('main')
        return reverse('admin2:static_page_detail', args=[self.id])
