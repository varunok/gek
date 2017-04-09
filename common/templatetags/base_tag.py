from django import template

from services.models import ServicesRieltor, Valuation, Repair, Insurance, Cleaning, InstallationWater, UniversalService

register = template.Library()


@register.assignment_tag
def service_rieltor_is_active():
    return ServicesRieltor.objects.get().is_enable


@register.assignment_tag
def service_rieltor_slug():
    return ServicesRieltor.objects.get().slug


@register.assignment_tag
def valuation_is_active():
    return Valuation.objects.get().is_enable


@register.assignment_tag
def valuation_slug():
    return Valuation.objects.get().slug


@register.assignment_tag
def repair_is_active():
    return Repair.objects.get().is_enable


@register.assignment_tag
def repair_slug():
    return Repair.objects.get().slug


@register.assignment_tag
def insurance_is_active():
    return Insurance.objects.get().is_enable


@register.assignment_tag
def insurance_slug():
    return Insurance.objects.get().slug


@register.assignment_tag
def cleaning_is_active():
    return Cleaning.objects.get().is_enable


@register.assignment_tag
def cleaning_slug():
    return Cleaning.objects.get().slug


@register.assignment_tag
def installation_water_is_active():
    return InstallationWater.objects.get().is_enable


@register.assignment_tag
def installation_water_slug():
    return InstallationWater.objects.get().slug


@register.assignment_tag
def universals():
    return UniversalService.objects.all()
