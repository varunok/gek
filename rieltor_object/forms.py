# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.widgets import CheckboxInput, Select, NumberInput, CheckboxSelectMultiple

from rieltor_object.models import Building, TypeDeal, TypeAppointment, TypeLocation, TypeFloor, TypeEntrance


def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering, 
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render

    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)

    cls.widget.render = _widget_render_wrapper

class FilterForm(forms.Form):
    type_deal = forms.IntegerField(
        widget=CheckboxSelectMultiple(
            choices=TypeDeal.CHOICES
        ),
        required=False,
    )
    appointment = forms.IntegerField(
        widget=Select(
            attrs={'id': 'type_ads'},
            choices=TypeAppointment.CHOICES,
        ),
        label='Тип недвижимости',
        required=False
    )
    price_from = forms.IntegerField(
        min_value=0,
        widget=NumberInput(
            attrs={'placeholder': 'От'}
        ),
        required=False,
    )
    price_to = forms.IntegerField(
        min_value=0,
        widget=NumberInput(
            attrs={'placeholder': 'До'}
        ),
        required=False,
    )
    set_field_html_name(price_from, 'price__gt')
    set_field_html_name(price_to, 'price__lt')
    footage_from = forms.IntegerField(
        min_value=0,
        widget=NumberInput(
            attrs={'placeholder': 'От'}
        ),
        required=False,
    )
    footage_to = forms.IntegerField(
        min_value=0,
        widget=NumberInput(
            attrs={'placeholder': 'До'}
        ),
        required=False,
    )
    set_field_html_name(footage_from, 'footage__gt')
    set_field_html_name(footage_to, 'footage__lt')
    location = forms.IntegerField(
        widget=CheckboxSelectMultiple(
            choices=TypeLocation.CHOICES
        ),
        required=False,
    )
    floor = forms.IntegerField(
        widget=CheckboxSelectMultiple(
            choices=TypeFloor.CHOICES
        ),
        required=False,
    )
    entrance = forms.IntegerField(
        widget=CheckboxSelectMultiple(
            choices=TypeEntrance.CHOICES
        ),
        required=False,
    )

    class Meta:
        model = Building
        fields = '__all__',