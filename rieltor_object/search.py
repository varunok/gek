# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import django_filters
from django_filters import STRICTNESS
from django_filters.filters import FilterMethod
from django_filters.widgets import CSVWidget

from rieltor_object.forms import FilterForm
from rieltor_object.models import Building, TypeEntrance, TypeLocation, TypeDeal, TypeFloor


class NumberInFilter(django_filters.MultipleChoiceFilter, django_filters.NumberFilter):
    pass


class BuildingFilter(django_filters.FilterSet):
    floor = django_filters.AllValuesMultipleFilter(choices=TypeFloor.CHOICES)
    type_deal = django_filters.AllValuesMultipleFilter(choices=TypeDeal.CHOICES)
    location = django_filters.AllValuesMultipleFilter(choices=TypeLocation.CHOICES)
    entrance = django_filters.AllValuesMultipleFilter(choices=TypeEntrance.CHOICES)
    class Meta:
        model = Building
        fields = {
            'price': ['lt', 'gt'],
            'footage': ['lt', 'gt'],
            'type_deal': ['in'],
            'location': ['in'],
            'floor': ['in'],
            'entrance': ['in'],
            'appointment': ['exact'],
        }


        # strict = STRICTNESS.RAISE_VALIDATION_ERROR
        # strict = STRICTNESS.RETURN_NO_RESULTS
        strict = STRICTNESS.IGNORE
        # form = FilterForm

