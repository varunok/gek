# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.contrib.sites.models import Site

from admin2.models import BuildingPageModel, OfisPageModel, DailyPageModel, NewBuildingPageModel, EarthPageModel, \
    SettingsAddress
from services.models import ServicesRieltor, Valuation, Repair, Insurance, Cleaning, InstallationWater, UniversalService

register = template.Library()


@register.assignment_tag
def service_rieltor_is_active():
    return ServicesRieltor.get_solo().is_enable


@register.assignment_tag
def service_rieltor_slug():
    return ServicesRieltor.get_solo().slug


@register.assignment_tag
def valuation_is_active():
    return Valuation.get_solo().is_enable


@register.assignment_tag
def valuation_slug():
    return Valuation.get_solo().slug


@register.assignment_tag
def repair_is_active():
    return Repair.get_solo().is_enable


@register.assignment_tag
def repair_slug():
    return Repair.get_solo().slug


@register.assignment_tag
def insurance_is_active():
    return Insurance.get_solo().is_enable


@register.assignment_tag
def insurance_slug():
    return Insurance.get_solo().slug


@register.assignment_tag
def cleaning_is_active():
    return Cleaning.get_solo().is_enable


@register.assignment_tag
def cleaning_slug():
    return Cleaning.get_solo().slug


@register.assignment_tag
def installation_water_is_active():
    return InstallationWater.get_solo().is_enable


@register.assignment_tag
def installation_water_slug():
    return InstallationWater.get_solo().slug


@register.assignment_tag
def universals():
    return UniversalService.objects.all()


@register.assignment_tag
def building_is_enable():
    return BuildingPageModel.get_solo().is_enable


@register.assignment_tag
def ofices_is_enable():
    return OfisPageModel.get_solo().is_enable


@register.assignment_tag
def daily_is_enable():
    return DailyPageModel.get_solo().is_enable


@register.assignment_tag
def newbuilding_is_enable():
    return NewBuildingPageModel.get_solo().is_enable


@register.assignment_tag
def earth_is_enable():
    return EarthPageModel.get_solo().is_enable


@register.filter(name='cut_last_char')
def cut_last_char(string):
    return string[:-1]


@register.assignment_tag
def domen():
    tmp = '<span class="site_name">{0}</span><span class="domen">{1}</span>'
    domen = Site.objects.get_current()
    name = domen.name.split('.')[0]
    domen = domen.name.replace(name, '')
    return tmp.format(name, domen)


@register.assignment_tag
def phone():
    return SettingsAddress.get_solo().phone


@register.assignment_tag
def city():
    return SettingsAddress.get_solo().city


@register.assignment_tag
def address():
    return SettingsAddress.get_solo().address


@register.assignment_tag
def email():
    return SettingsAddress.get_solo().email

