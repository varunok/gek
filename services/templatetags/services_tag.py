import random

from django import template

from services.helpers import return_list_services

register = template.Library()


@register.assignment_tag
def service_list():
    active_service = return_list_services()
    if len(active_service) <= 4:
        return active_service
    list_service = []
    for i in range(0, 4):
        rand_item = random.choice(active_service)
        list_service.append(rand_item)
        active_service.remove(rand_item)
    return list_service


@register.assignment_tag
def service_list_downbar():
    return return_list_services()