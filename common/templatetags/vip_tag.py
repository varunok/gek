import random
from itertools import chain

from django import template

from rieltor_object.models import Ofice, Building

register = template.Library()


@register.assignment_tag
def vips():
    office = Ofice.objects.vips().order_by('?')[:2]
    building = Building.objects.vips().order_by('?')[:2]
    result = list(chain(building, office))
    return result
