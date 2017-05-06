# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import django_filters
from django import forms
from django.forms import CheckboxSelectMultiple, NumberInput, SelectDateWidget, Select
from django.utils.timezone import now
from django_filters import STRICTNESS

from rieltor_object.models import Building, Ofice, NewBuilding, TypeEntrance, TypeLocation, TypeDeal, TypeFloor, Daily


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    field_class = forms.IntegerField
    # pass


class FilterObjectMixin(django_filters.FilterSet):
    floor = django_filters.MultipleChoiceFilter(
        # widget=CheckboxSelectMultiple(choices=TypeFloor.CHOICES),
        choices=TypeFloor.CHOICES,
        required=False,
        lookup_expr='in',
    )
    type_deal = django_filters.MultipleChoiceFilter(
        choices=TypeDeal.CHOICES,
        required=False,
        lookup_expr='in',
    )
    location = django_filters.MultipleChoiceFilter(
        # widget=CheckboxSelectMultiple(choices=TypeLocation.CHOICES),
        choices=TypeLocation.CHOICES,
        required=False,
        lookup_expr='in',
    )
    entrance = django_filters.MultipleChoiceFilter(
        # widget=CheckboxSelectMultiple(choices=TypeEntrance.CHOICES),
        choices=TypeEntrance.CHOICES,
        required=False,
        lookup_expr='in',
    )
    # price__lt = django_filters.NumberFilter(
    #     widget=NumberInput(
    #         attrs={'placeholder': 'До'}
    #     ),
    #     name='price__lt',
    #     lookup_expr='lt',
    # )
    # price__gt = django_filters.NumberFilter(
    #     widget=NumberInput(
    #         attrs={'placeholder': 'От'}
    #     ),
    #     name='price__gt',
    #     lookup_expr='gt',
    # )
    # footage__lt = django_filters.NumberFilter(
    #     widget=NumberInput(
    #         attrs={'placeholder': 'До'}
    #     ),
    #     name='footage__lt',
    #     lookup_expr='lt',
    # )
    # footage__gt = django_filters.NumberFilter(
    #     widget=NumberInput(
    #         attrs={'placeholder': 'От'}
    #     ),
    #     name='footage__gt',
    #     lookup_expr='gt',
    # )


class FilterBuilding(FilterObjectMixin):
    class Meta:
        model = Building
        fields = {
            'appointment': ['exact'],
            'footage': ['gt', 'lt'],
            'price': ['gt', 'lt'],
        }
        # strict = STRICTNESS.RAISE_VALIDATION_ERROR
        strict = STRICTNESS.RETURN_NO_RESULTS
        # strict = STRICTNESS.IGNORE


class FilterOfise(FilterObjectMixin):
    class Meta:
        model = Ofice
        fields = {
            'appointment': ['exact'],
            'footage': ['gt', 'lt'],
            'price': ['gt', 'lt'],
        }
        # strict = STRICTNESS.RAISE_VALIDATION_ERROR
        strict = STRICTNESS.RETURN_NO_RESULTS
        # strict = STRICTNESS.IGNORE


class FilterNewBuilding(django_filters.FilterSet):
    price__lt = django_filters.NumberFilter(
        widget=NumberInput(
            attrs={'placeholder': 'До'}
        ),
        name='price__lt',
        lookup_expr='lt',
    )
    price__gt = django_filters.NumberFilter(
        widget=NumberInput(
            attrs={'placeholder': 'От'}
        ),
        name='price__gt',
        lookup_expr='gt',
    )
    total_area__lt = django_filters.NumberFilter(
        widget=NumberInput(
            attrs={'placeholder': 'До'}
        ),
        name='total_area__lt',
        lookup_expr='lt',
    )
    total_area__gt = django_filters.NumberFilter(
        widget=NumberInput(
            attrs={'placeholder': 'От'}
        ),
        name='total_area__gt',
        lookup_expr='gt',
    )
    start_construction = django_filters.DateFromToRangeFilter(
        widget=SelectDateWidget(
            years=range(1950, now().year+1),
            attrs={'style': 'width:32.5%;'}
        ),
    )
    end_construction = django_filters.DateFromToRangeFilter(
        widget=SelectDateWidget(
            years=range(1950, now().year+1),
            attrs={'style': 'width:32.5%;'}
        ),
    )
    class Meta:
        model = NewBuilding
        fields = {
            'district': ['in'],
            # 'start_construction': ['exact']
            # 'appointment': ['exact'],
        }


class FilterDaily(django_filters.FilterSet):
    rooms = django_filters.AllValuesFilter(
        widget=Select(),
        lookup_expr='exact',
        exclude='null'
    )
    class Meta:
        model = Daily
        fields = {
            'district': ['in'],
            'price': ['gt', 'lt'],
            # 'appointment': ['exact'],
        }

