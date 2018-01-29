# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext_lazy as _


class SuperlandingSettings(SingletonModel):
    enabled = models.BooleanField(
        default=False,
        verbose_name=_('Вкл/Викл')
    )

    def __unicode__(self):
        return '{0}'.format(self.id)

    class Meta:
        verbose_name = _('Настройки суперлендинга')