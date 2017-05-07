import random

from django import template

from rieltor_object.models import Ofice, Building

register = template.Library()


@register.assignment_tag
def vips():
    try:
        bool_rand = bool(random.getrandbits(1))
        print (bool_rand)
        if bool_rand:
            return Ofice.objects.vips().order_by('?')[:3]
        else:
            return Building.objects.vips().order_by('?')[:3]
    except:
        return ''
