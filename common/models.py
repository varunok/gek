# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.urls import reverse_lazy, reverse


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
        verbose_name='Дата создания',
        auto_now_add=True
    )
    source = models.TextField(
        verbose_name='Источник'
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
    address = models.CharField(
        verbose_name='Адрес',
        max_length=300,
        blank=True,
        null=True
    )
    price = models.CharField(
        verbose_name='Цена',
        max_length=300,
        blank=True,
        null=True
    )
    text = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        null=True
    )
    comming = models.TextField(
        verbose_name='Заезд',
        blank=True,
        null=True
    )
    go = models.TextField(
        verbose_name='Отьезд',
        blank=True,
        null=True
    )


    def __unicode__(self):
        return '%s' % (self.id)

    def save(self, *args, **kwargs):
        if self.comming:
            self.text = '{0}.Заезд: {1}'.format(self.text, self.comming)
        if self.go:
            self.text = '{0}.Отьезд: {1}'.format(self.text, self.go)
        super(Application, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created']


class Video(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
        blank=True,
        null=True
    )
    video = models.TextField(
        verbose_name='Код видео',
        blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ModelInService.model_in}
    )
    is_enable = models.BooleanField(
        verbose_name='Включен ли?',
        default=True
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title if self.title else self.id)


class FAQ(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
        blank=True,
        null=True
    )
    text = models.TextField(
        verbose_name='Текст',
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
        verbose_name = 'ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ'
        verbose_name_plural = 'ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title if self.title else self.id)


class TableRepair(models.Model):
    name = models.CharField(
        verbose_name='Наименование работ',
        max_length=250,
        blank=True,
        null=True
    )
    price = models.CharField(
        verbose_name='Стоимость',
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
        verbose_name = 'Стоимость ремонта'
        verbose_name_plural = 'Стоимость ремонта'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.name if self.name else self.id)


class Photo(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Фото',
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
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

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
        verbose_name = 'Текст пакета'
        verbose_name_plural = 'Текст пакетов'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.id)


class BasePacket(models.Model):
    __name_packet__ = 'base_packet'
    title = models.CharField(
        verbose_name='Начинающий',
        max_length=250,
        default='Начинающий',
        blank=True
    )
    text = GenericRelation(TextPacket, related_query_name='basepacket')

    class Meta:
        verbose_name = 'Пакет Начинающий'
        verbose_name_plural = 'Пакет Начинающий'

    def __unicode__(self):
        return '{} - ID:{}'.format(self.title, self.id)


class MidlePacket(models.Model):
    __name_packet__ = 'midle_packet'
    title = models.CharField(
        verbose_name='Продвинутый',
        max_length=250,
        default='Продвинутый',
        blank=True
    )
    text = GenericRelation(TextPacket, related_query_name='midlepacket')

    class Meta:
        verbose_name = 'Пакет Продвинутый'
        verbose_name_plural = 'Пакет Продвинутый'

    def __unicode__(self):
        return '{} - ID:{}'.format(self.title, self.id)


class ExpertPacket(models.Model):
    __name_packet__ = 'expert_packet'
    title = models.CharField(
        verbose_name='Эксперт',
        max_length=250,
        default='Эксперт',
        blank=True
    )
    text = GenericRelation(TextPacket, related_query_name='expertpacket')

    class Meta:
        verbose_name = 'Пакет Эксперт'
        verbose_name_plural = 'Пакет Эксперт'

    def __unicode__(self):
        return '{} - ID:{}'.format(self.title, self.id)


class Advantage(models.Model):
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Фото',
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
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.id)


class ApartmentNext(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250
    )
    value = models.IntegerField(
        verbose_name='Значение',
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
        verbose_name = 'Рядом с квартирой'
        verbose_name_plural = 'Рядом с квартирой'
        ordering = ['-id']

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.id)


class Feed(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=250,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=250,
        blank=True,
        null=True
    )
    feed = models.TextField(
        verbose_name='Отзив',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Фото',
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
        verbose_name = 'Отзив'
        verbose_name_plural = 'Отзивы'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.name if self.name else self.id)


class Schedule(models.Model):
    MO = 'Понедельник'
    TU = 'Вторник'
    WE = 'Среда'
    TH = 'Четверг'
    FR = 'Пятница'
    SA = 'Суббота'
    SU = 'Воскресенье'
    CHOICES = (
        (MO, 'Понедельник'),
        (TU, 'Вторник'),
        (WE, 'Среда'),
        (TH, 'Четверг'),
        (FR, 'Пятница'),
        (SA, 'Суббота'),
        (SU, 'Воскресенье'),
    )
    day = models.CharField(
        verbose_name='День недели',
        max_length=25,
        choices=CHOICES,
        blank=True, null=True
    )
    open_from = models.TimeField(
        verbose_name='Часов От',
        blank=True, null=True
    )
    open_to = models.TimeField(
        verbose_name='Часов До',
        blank=True, null=True
    )
    special = models.CharField(
        verbose_name='Cобственное значение',
        max_length=250,
        blank=True, null=True,
        help_text='Другое будет игнорироватся'
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
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'
        # ordering = ['-id']

    def __unicode__(self):
        if self.special:
            return '{} - {}'.format(self.content_type, self.special)
        return '{} - {} c {} до {}'.format(self.content_type, self.day, self.open_from, self.open_to)


class WhatYouKnown(models.Model):
    text = models.TextField(
        verbose_name='Текст',
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
        verbose_name = 'Что вы узнаете'
        verbose_name_plural = 'Что вы узнаете'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.text)


class PriorityChoices(object):
    HARD = 'Сложное'
    LOW = 'Простое'
    MIDDLE = 'Среднее'
    CHOICES = (
        (HARD, 'Сложное'),
        (LOW, 'Простое'),
        (MIDDLE, 'Среднее'),
    )

    model__in = ('salebuildplan',)


class Preparation(models.Model):
    title = models.TextField(
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        null=True
    )
    priority = models.CharField(
        verbose_name='Приоритет задания',
        choices=PriorityChoices.CHOICES,
        max_length=20,
        blank=True,
        null=True
    )
    when_do = models.DateField(
        verbose_name='Когда приступите?',
        blank=True,
        null=True
    )
    plan_do = models.DateField(
        verbose_name='Планируете выполнить',
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
        verbose_name = 'Подготовка'
        verbose_name_plural = 'Подготовки'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title)

    def get_absolute_url(self):
        success_url = reverse('admin2:plan_preparations')


class Process(models.Model):
    title = models.TextField(
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        null=True
    )
    priority = models.CharField(
        verbose_name='Приоритет задания',
        choices=PriorityChoices.CHOICES,
        max_length=20,
        blank=True,
        null=True
    )
    when_do = models.DateField(
        verbose_name='Когда приступите?',
        blank=True,
        null=True
    )
    plan_do = models.DateField(
        verbose_name='Планируете выполнить',
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
        verbose_name = 'Процесс'
        verbose_name_plural = 'Процесс'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title)

    def get_absolute_url(self):
        success_url = reverse('admin2:plan_process')


class Finish(models.Model):
    title = models.TextField(
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        null=True
    )
    priority = models.CharField(
        verbose_name='Приоритет задания',
        choices=PriorityChoices.CHOICES,
        max_length=20,
        blank=True,
        null=True
    )
    when_do = models.DateField(
        verbose_name='Когда приступите?',
        blank=True,
        null=True
    )
    plan_do = models.DateField(
        verbose_name='Планируете выполнить',
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
        verbose_name = 'Завершение'
        verbose_name_plural = 'Завершение'

    def __unicode__(self):
        return '{} - {}'.format(self.content_type, self.title)

    def get_absolute_url(self):
        success_url = reverse('admin2:plan_finish')

