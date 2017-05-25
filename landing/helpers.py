# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from itertools import chain

from django.contrib.sites.models import Site

from rieltor_object.models import Building, Ofice
from seo.models import SEO


def query_landing(filter):
    building = Building.objects.all()
    office = Ofice.objects.all()
    if filter.type_deal == 'rent' or filter.type_deal == 'sale':
        building = building.filter(type_deal=filter.type_deal)
        office = office.filter(type_deal=filter.type_deal)
    if filter.type_property:
        building = building.filter(appointment__in=filter.type_property)
        office = office.filter(appointment__in=filter.type_property)
    if filter.price_gt:
        building = building.filter(price__gte=filter.price_gt)
        office = office.filter(price__gte=filter.price_gt)
    if filter.price_lt:
        building = building.filter(price__lte=filter.price_lt)
        office = office.filter(price__lte=filter.price_lt)
    if filter.footage_gt:
        building = building.filter(footage__gte=filter.footage_gt)
        office = office.filter(footage__gte=filter.footage_gt)
    if filter.footage_lt:
        building = building.filter(footage__lte=filter.footage_lt)
        office = office.filter(footage__lte=filter.footage_lt)
    if filter.rooms:
        building = building.filter(rooms__exact=filter.rooms)
        office = office.filter(rooms__exact=filter.rooms)
    if filter.district:
        building = building.filter(district=filter.district)
        office = office.filter(district=filter.district)
    result = list(chain(building, office))
    random.shuffle(result)
    return result


def get_seo(request):
    path = str(Site.objects.get_current()) + request.get_full_path()
    if SEO.objects.filter(url=path).exists():
        seo = SEO.objects.filter(url=path).first()
        return seo
    return None
