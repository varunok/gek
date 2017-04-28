# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from common.helpers import get_client_ip

register = template.Library()


@register.filter(name='fav_is_active')
def fav_is_active(obj, request):
    ip = get_client_ip(request)
    if obj.favorites.filter(ip=ip).exists():
        return 'active'
    return None