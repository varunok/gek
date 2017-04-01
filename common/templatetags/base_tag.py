from django import template

from services.models import ServicesRieltor

register = template.Library()


@register.assignment_tag
def service_rieltor_is_active():
    return ServicesRieltor.objects.get().is_enable

@register.assignment_tag
def service_rieltor_slug():
    return ServicesRieltor.objects.get().slug