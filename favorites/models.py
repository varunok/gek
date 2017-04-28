# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from rieltor_object.models import NewBuilding, Building, Ofice, Daily, Earth


class Favorites(models.Model):
    ip = models.GenericIPAddressField()
    newbuildings = models.ManyToManyField(
        NewBuilding,
        blank=True,
        related_name='favorites'
    )
    buildings = models.ManyToManyField(
        Building,
        blank=True,
        related_name='favorites'
    )
    offices = models.ManyToManyField(
        Ofice,
        blank=True,
        related_name='favorites'
    )
    dailys = models.ManyToManyField(
        Daily,
        blank=True,
        related_name='favorites'
    )
    earth = models.ManyToManyField(
        Earth,
        blank=True,
        related_name='favorites'
    )
