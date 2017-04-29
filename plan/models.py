# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from solo.models import SingletonModel

from common.models import Photo, Preparation, Process, Finish


class PlanPage(SingletonModel):
    name = models.CharField(
        default='Планы',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
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
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    video = models.TextField(
        verbose_name='Код видео',
        blank=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    point1 = models.CharField(
        verbose_name='Пункт 1',
        max_length=50,
        blank=True,
        null=True
    )
    point2 = models.CharField(
        verbose_name='Пункт 2',
        max_length=50,
        blank=True,
        null=True
    )
    point3 = models.CharField(
        verbose_name='Пункт 3',
        max_length=50,
        blank=True,
        null=True
    )
    point4 = models.CharField(
        verbose_name='Пункт 4',
        max_length=50,
        blank=True,
        null=True
    )
    point5 = models.CharField(
        verbose_name='Пункт 5',
        max_length=50,
        blank=True,
        null=True
    )
    images = GenericRelation(Photo, related_query_name='planpage')

    class Meta:
        verbose_name = 'Планы'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('main')

    def get_edit_url(self):
        return reverse('admin2:plan')

    def meta(self):
        return self._meta


class SaleBuildPlan(SingletonModel):
    name = models.CharField(
        default='Продать помещения',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    preparations = GenericRelation(Preparation, related_query_name='salebuildplan')
    process = GenericRelation(Process, related_query_name='salebuildplan')
    finishes = GenericRelation(Finish, related_query_name='salebuildplan')
    class Meta:
        verbose_name = 'Продать помещения'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('admin2:sale_build_plan')

    def get_edit_url(self):
        return reverse('admin2:sale_build_plan')

    def meta(self):
        return self._meta


class BuyBuildPlan(SingletonModel):
    name = models.CharField(
        default='Купить помещения',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    preparations = GenericRelation(Preparation, related_query_name='buybuildplan')
    process = GenericRelation(Process, related_query_name='buybuildplan')
    finishes = GenericRelation(Finish, related_query_name='buybuildplan')
    class Meta:
        verbose_name = 'Купить помещения'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('admin2:buy_build_plan')

    def get_edit_url(self):
        return reverse('admin2:buy_build_plan')

    def meta(self):
        return self._meta


class RentBuildPlan(SingletonModel):
    name = models.CharField(
        default='Арендовать помещения',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    preparations = GenericRelation(Preparation, related_query_name='rentbuildplan')
    process = GenericRelation(Process, related_query_name='rentbuildplan')
    finishes = GenericRelation(Finish, related_query_name='rentbuildplan')
    class Meta:
        verbose_name = 'Арендовать помещения'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('admin2:rent_build_plan')

    def get_edit_url(self):
        return reverse('admin2:rent_build_plan')

    def meta(self):
        return self._meta


class PassBuildPlan(SingletonModel):
    name = models.CharField(
        default='Сдать недвижимость',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    preparations = GenericRelation(Preparation, related_query_name='passbuildplan')
    process = GenericRelation(Process, related_query_name='passbuildplan')
    finishes = GenericRelation(Finish, related_query_name='passbuildplan')
    class Meta:
        verbose_name = 'Сдать недвижимость'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('admin2:pass_build_plan')

    def get_edit_url(self):
        return reverse('admin2:pass_build_plan')

    def meta(self):
        return self._meta


class RepairBuildPlan(SingletonModel):
    name = models.CharField(
        default='Ремонт недвижимости',
        verbose_name='Название',
        max_length=30,
        unique=True,
        editable=False
    )
    title = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='background/%Y/%m/%d/',
        blank=True
    )
    preparations = GenericRelation(Preparation, related_query_name='repairbuildplan')
    process = GenericRelation(Process, related_query_name='repairbuildplan')
    finishes = GenericRelation(Finish, related_query_name='repairbuildplan')
    class Meta:
        verbose_name = 'Ремонт недвижимости'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('admin2:repair_build_plan')

    def get_edit_url(self):
        return reverse('admin2:repair_build_plan')

    def meta(self):
        return self._meta