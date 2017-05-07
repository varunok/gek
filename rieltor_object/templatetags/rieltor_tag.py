# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from easy_thumbnails.files import get_thumbnailer

from django import template
from banners.models import SideBanner, DownBanner

register = template.Library()


@register.simple_tag(name='filterpath')
def filterpath(url, name, value, *args):
    if isinstance(value, int):
        value = unicode(value)
    if url[-1] == '/':
        url = url[:-1]
    args = args or ()
    try:
        list_ele = []
        empty, val1, val2, elements = url.split('/')
        category = '/' + val1 + '/' + val2
        elements = group(elements.split('-'), 2)
        for ele in elements:
            if (name, value) != ele and args != ele:
                ele = '-'.join(ele)
                list_ele.append(ele)
        list_ele = '-'.join(list_ele)
        url = '/'.join([category, list_ele])
    except:
        return ''
    return url

def group(iterable, count):
    return zip(*[iter(iterable)] * count)

