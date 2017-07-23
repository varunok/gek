# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext_lazy as _


class ModelInService(object):
    model_in = (
        'servicesrieltor',
        'valuation',
        'repair',
        'insurance',
        'cleaning',
        'installationwater',
        'universalservice',
        'building',
        'trustpagemodel'
    )


class Application(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True
    )
    source = models.TextField(
        verbose_name=_('Источник')
    )
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=100,
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name=_('Телефон'),
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
    address = models.CharField(
        verbose_name=_('Адрес'),
        max_length=300,
        blank=True,
        null=True
    )
    price = models.CharField(
        verbose_name=_('Цена'),
        max_length=300,
        blank=True,
        null=True
    )
    text = models.TextField(
        verbose_name=_('Комментарий'),
        blank=True,
        null=True
    )
    comming = models.TextField(
        verbose_name=_('Заезд'),
        blank=True,
        null=True
    )
    go = models.TextField(
        verbose_name=_('Отьезд'),
        blank=True,
        null=True
    )
    is_reading = models.BooleanField(
        default=False
    )
    custom_id = models.PositiveIntegerField(
        verbose_name='ID',
        blank=True,
        null=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        # limit_choices_to={'model__in': somsing}
    )
    object_id = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    content_object = GenericForeignKey('content_type', 'object_id')


    def __unicode__(self):
        return '%s' % (self.id)

    def save(self, *args, **kwargs):
        if self.comming:
            self.text = '{0}.Заезд: {1}'.format(self.text, self.comming)
        if self.go:
            self.text = '{0}.Отьезд: {1}'.format(self.text, self.go)
        super(Application, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')
        ordering = ['-created']


class Video(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=250,
        blank=True,
        null=True
    )
    video = models.TextField(
        verbose_name=_('Код видео'),
        blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ModelInService.model_in}
    )
    is_enable = models.BooleanField(
        verbose_name=_('Включен ли?'),
        default=True
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Видео')
        verbose_name_plural = _('Видео')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title if self.title else self.id)


class FAQ(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=250,
        blank=True,
        null=True
    )
    text = models.TextField(
        verbose_name=_('Текст'),
        blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ModelInService.model_in}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ')
        verbose_name_plural = _('ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title if self.title else self.id)


class TableRepair(models.Model):
    name = models.CharField(
        verbose_name=_('Наименование работ'),
        max_length=250,
        blank=True,
        null=True
    )
    price = models.CharField(
        verbose_name=_('Стоимость'),
        max_length=250,
        blank=True,
        null=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ModelInService.model_in}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Стоимость ремонта')
        verbose_name_plural = _('Стоимость ремонта')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.name if self.name else self.id)


class Photo(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=250,
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='photos/%Y/%m/%d/',
        blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ModelInService.model_in}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Фото')
        verbose_name_plural = _('Фото')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title if self.title else self.id)


class TextPacket(models.Model):
    text = models.TextField(verbose_name='Текст')

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('basepacket',
                                        'midlepacket',
                                        'expertpacket'
                                        )}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Текст пакета')
        verbose_name_plural = _('Текст пакетов')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.id)


class BasePacket(models.Model):
    __name_packet__ = 'base_packet'
    title = models.CharField(
        verbose_name=_('Начинающий'),
        max_length=250,
        default=_('Начинающий'),
        blank=True
    )
    text = GenericRelation(TextPacket, related_query_name='basepacket')

    class Meta:
        verbose_name = _('Пакет Начинающий')
        verbose_name_plural = _('Пакет Начинающий')

    def __unicode__(self):
        return '{} - ID:{}'.format(self.title, self.id)


class MidlePacket(models.Model):
    __name_packet__ = 'midle_packet'
    title = models.CharField(
        verbose_name=_('Продвинутый'),
        max_length=250,
        default=_('Продвинутый'),
        blank=True
    )
    text = GenericRelation(TextPacket, related_query_name='midlepacket')

    class Meta:
        verbose_name = _('Пакет Продвинутый')
        verbose_name_plural = _('Пакет Продвинутый')

    def __unicode__(self):
        return '{} - ID:{}'.format(self.title, self.id)


class ExpertPacket(models.Model):
    __name_packet__ = 'expert_packet'
    title = models.CharField(
        verbose_name=_('Эксперт'),
        max_length=250,
        default=_('Эксперт'),
        blank=True
    )
    text = GenericRelation(TextPacket, related_query_name='expertpacket')

    class Meta:
        verbose_name = _('Пакет Эксперт')
        verbose_name_plural = _('Пакет Эксперт')

    def __unicode__(self):
        return '{} - ID:{}'.format(self.title, self.id)


class Advantage(models.Model):
    description = models.TextField(
        verbose_name=_('Описание')
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='photos/%Y/%m/%d/',
        blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('universalservice',)}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _("Преимущество")
        verbose_name_plural = _("Преимущества")

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.id)


class ApartmentNext(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=250
    )
    value = models.IntegerField(
        verbose_name=_('Значение'),
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('daily',
                                        )}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Рядом с квартирой')
        verbose_name_plural = _('Рядом с квартирой')
        ordering = ['-id']

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.id)


class Feed(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=250,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name=_('Город'),
        max_length=250,
        blank=True,
        null=True
    )
    feed = models.TextField(
        verbose_name=_('Отзив'),
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to='feed/%Y/%m/%d/',
        blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('trustpagemodel',
                                        )}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Отзив')
        verbose_name_plural = _('Отзивы')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.name if self.name else self.id)


class Schedule(models.Model):
    MO = _('Понедельник')
    TU = _('Вторник')
    WE = _('Среда')
    TH = _('Четверг')
    FR = _('Пятница')
    SA = _('Суббота')
    SU = _('Воскресенье')
    CHOICES = (
        (MO, _('Понедельник')),
        (TU, _('Вторник')),
        (WE, _('Среда')),
        (TH, _('Четверг')),
        (FR, _('Пятница')),
        (SA, _('Суббота')),
        (SU, _('Воскресенье')),
    )
    day = models.CharField(
        verbose_name=_('День недели'),
        max_length=25,
        choices=CHOICES,
        blank=True, null=True
    )
    open_from = models.TimeField(
        verbose_name=_('Часов От'),
        blank=True, null=True
    )
    open_to = models.TimeField(
        verbose_name=_('Часов До'),
        blank=True, null=True
    )
    special = models.CharField(
        verbose_name=_('Cобственное значение'),
        max_length=250,
        blank=True, null=True,
        help_text=_('Другое будет игнорироватся')
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('contactpagemodel',
                                        )}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('График работы')
        verbose_name_plural = _('График работы')
        # ordering = ['-id']

    def __unicode__(self):
        if self.special:
            return '{} - {}'.format(self.content_type, self.special)
        return '{} - {} c {} до {}'.format(self.content_type, self.day, self.open_from, self.open_to)


class WhatYouKnown(models.Model):
    text = models.TextField(
        verbose_name=_('Текст'),
        blank=True,
        null=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('videos',
                                        )}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Что вы узнаете')
        verbose_name_plural = _('Что вы узнаете')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.text)


class PriorityChoices(object):
    HARD = _('Сложное')
    LOW = _('Простое')
    MIDDLE = _('Среднее')
    CHOICES = (
        (HARD, _('Сложное')),
        (LOW, _('Простое')),
        (MIDDLE, _('Среднее')),
    )

    model__in = ('salebuildplan',)


class Preparation(models.Model):
    title = models.TextField(
        verbose_name=_('Заголовок')
    )
    description = models.TextField(
        verbose_name=_('Описание')
    )
    comment = models.TextField(
        verbose_name=_('Комментарий'),
        blank=True,
        null=True
    )
    priority = models.CharField(
        verbose_name=_('Приоритет задания'),
        choices=PriorityChoices.CHOICES,
        max_length=20,
        blank=True,
        null=True
    )
    when_do = models.DateField(
        verbose_name=_('Когда приступите?'),
        blank=True,
        null=True
    )
    plan_do = models.DateField(
        verbose_name=_('Планируете выполнить'),
        blank=True,
        null=True
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': PriorityChoices.model__in}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Подготовка')
        verbose_name_plural = _('Подготовки')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title)

    def get_absolute_url(self):
        success_url = reverse('admin2:plan_preparations')


class Process(models.Model):
    title = models.TextField(
        verbose_name=_('Заголовок')
    )
    description = models.TextField(
        verbose_name=_('Описание')
    )
    comment = models.TextField(
        verbose_name=_('Комментарий'),
        blank=True,
        null=True
    )
    priority = models.CharField(
        verbose_name=_('Приоритет задания'),
        choices=PriorityChoices.CHOICES,
        max_length=20,
        blank=True,
        null=True
    )
    when_do = models.DateField(
        verbose_name=_('Когда приступите?'),
        blank=True,
        null=True
    )
    plan_do = models.DateField(
        verbose_name=_('Планируете выполнить'),
        blank=True,
        null=True
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': PriorityChoices.model__in}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Процесс')
        verbose_name_plural = _('Процесс')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title)

    def get_absolute_url(self):
        success_url = reverse('admin2:plan_process')


class Finish(models.Model):
    title = models.TextField(
        verbose_name=_('Заголовок')
    )
    description = models.TextField(
        verbose_name=_('Описание')
    )
    comment = models.TextField(
        verbose_name=_('Комментарий'),
        blank=True,
        null=True
    )
    priority = models.CharField(
        verbose_name=_('Приоритет задания'),
        choices=PriorityChoices.CHOICES,
        max_length=20,
        blank=True,
        null=True
    )
    when_do = models.DateField(
        verbose_name=_('Когда приступите?'),
        blank=True,
        null=True
    )
    plan_do = models.DateField(
        verbose_name=_('Планируете выполнить'),
        blank=True,
        null=True
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': PriorityChoices.model__in}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Завершение')
        verbose_name_plural = _('Завершение')

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title)

    def get_absolute_url(self):
        success_url = reverse('admin2:plan_finish')

