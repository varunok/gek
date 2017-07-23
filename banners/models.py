# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse
from solo.models import SingletonModel

from django.utils.translation import ugettext_lazy as _


class DownBanner(SingletonModel):
    code = models.TextField(
        verbose_name=_('Код баннера'),
        blank=True,
        null=True
    )
    active_code = models.BooleanField(
        default=False
    )
    image = models.ImageField(
        verbose_name=_('Картинка'),
        upload_to='banner/%Y/%m/%d/',
        blank=True
    )
    link = models.URLField(
        verbose_name=_('Ссылка'),
        help_text='http://example.com',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Нижний баннер')

    def __unicode__(self):
        return 'Нижний баннер (970х250)'

    def get_edit_image_url(self):
        return reverse('admin2:downbanners_image')

    def get_edit_code_url(self):
        return reverse('admin2:downbanners_code')


class SideBanner(SingletonModel):
    code = models.TextField(
        verbose_name=_('Код баннера'),
        blank=True,
        null=True
    )
    active_code = models.BooleanField(
        default=False
    )
    image = models.ImageField(
        verbose_name=_('Картинка'),
        upload_to='banner/%Y/%m/%d/',
        blank=True
    )
    link = models.URLField(
        verbose_name=_('Ссылка'),
        help_text='http://example.com',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Боковой баннер')

    def __unicode__(self):
        return 'Боковой баннер (240х400)'

    def get_edit_image_url(self):
        return reverse('admin2:sidebanners_image')

    def get_edit_code_url(self):
        return reverse('admin2:sidebanners_code')
