# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.


class ModelInService(object):
    model_in = (
        'servicesrieltor',
        'valuation',
        'repair',
        'insurance',
        'cleaning',
        'installationwater',
        'universalservice',
        'building'
    )


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
