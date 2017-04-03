from django import template

from services.models import ServicesRieltor, Valuation

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