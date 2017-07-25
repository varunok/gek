# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import django_filters
from django import forms
from django.forms import Select, TextInput
from django_filters import STRICTNESS
from django.utils.translation import ugettext_lazy as _

from rieltor_object.models import Building, Ofice, NewBuilding, TypeEntrance, TypeLocation, TypeDeal, TypeFloor, Daily, \
    DailyDistrict, District, Earth, EarthDistrict


class NumberInFilter(django_filters.NumberFilter):
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



class FilterBuilding(django_filters.FilterSet):
    ROOMS_CHOICES = (
        (1, _('1-но комнатные')),
        (2, _('2-но комнатные')),
        (3, _('3-но комнатные')),
        (4, _('4-но комнатные')),
        (5, _('Многокомнатные')),
    )
    type_deal = django_filters.MultipleChoiceFilter(
        choices=TypeDeal.CHOICES,
        required=False,
        lookup_expr='in',
    )
    district = django_filters.ModelChoiceFilter(
        widget=Select(),
        queryset=District.objects.all()
    )
    rooms = django_filters.ChoiceFilter(
        choices=ROOMS_CHOICES,
        method='rooms_choice'
    )
    class Meta:
        model = Building
        fields = {
            'proposal': ['exact'],
            'period': ['exact'],
            'appointment': ['exact'],
            'layout': ['exact'],
            'footage': ['gt', 'lt'],
            'price': ['gt', 'lt'],
            'floor': ['gte', 'lte'],
        }
        # strict = STRICTNESS.RAISE_VALIDATION_ERROR
        strict = STRICTNESS.RETURN_NO_RESULTS
        # strict = STRICTNESS.IGNORE

    def rooms_choice(self, queryset, name, value):
        if isinstance(value, unicode):
            value = int(value)
        if value >= 5:
            lookup = '__'.join([name, 'gt'])
        else:
            lookup = '__'.join([name, 'exact'])
        return queryset.filter(**{lookup: value})


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
    district = django_filters.ModelChoiceFilter(
        widget=Select(),
        queryset=District.objects.all()
    )
    end_construction = django_filters.DateFilter(
        widget=TextInput(
            attrs={'class': 'datepicker_c',
                   'style': 'width:310px;'}
        ),
    )
    class Meta:
        model = NewBuilding
        fields = {
            # 'district': ['in'],
            'price': ['gt', 'lt'],
            'price_object': ['gt', 'lt'],
            'total_area': ['gt', 'lt'],
            # 'start_construction': ['exact']
            # 'appointment': ['exact'],
        }
        strict = STRICTNESS.RETURN_NO_RESULTS


class FilterDaily(django_filters.FilterSet):
    rooms = django_filters.AllValuesFilter(
        widget=Select(),
        lookup_expr='exact',
    )
    sleeping_places = django_filters.AllValuesFilter(
        widget=Select(),
        lookup_expr='exact',
    )
    district = django_filters.ModelChoiceFilter(
        widget=Select(),
        queryset=DailyDistrict.objects.all()
    )
    class Meta:
        model = Daily
        fields = {
            'price': ['gt', 'lt'],
        }
        strict = STRICTNESS.RETURN_NO_RESULTS


class FilterEarth(django_filters.FilterSet):
    district = django_filters.ModelChoiceFilter(
        widget=Select(),
        queryset=EarthDistrict.objects.all()
    )
    class Meta:
        model = Earth
        fields = {
            'area': ['gt', 'lt'],
            'price': ['gt', 'lt'],
            'type_area': ['exact'],
        }
        strict = STRICTNESS.RETURN_NO_RESULTS

