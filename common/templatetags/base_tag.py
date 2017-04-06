from django import template

from services.models import ServicesRieltor, Valuation, Repair, Insurance

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