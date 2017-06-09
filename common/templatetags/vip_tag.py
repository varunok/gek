import random
from itertools import chain

from django import template

from rieltor_object.models import Ofice, Building

register = template.Library()


@register.assignment_tag
def vips():
    office = Ofice.objects.vips().order_by('?')
    building = Building.objects.vips().order_by('?')
    result = list(chain(building, office))
    list_vip = []
    if len(result) == 1:
        return result
    if len(result) > 1:
        for i in range(0, 3):
            rand_item = random.choice(result)
            list_vip.append(rand_item)
            result.remove(rand_item)
    return list_vip
