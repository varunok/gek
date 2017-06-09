# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import QueryDict

from admin2.models import SettingsAddress
from rieltor_object.models import TypeDeal, TypeAppointment, TypeAppointmentOffice, District


class HelperFilter(object):
    qd = None

    def __init__(self, request):
        self.request = request
        self.mutable_path(self.get_path(self.request))

    def get_path(self, request):
        return request.path

    def mutable_path(self, path):
        if path[-1] == '/':
            path = path[:-1]
        element = self.group(path.split('/')[-1].split('-'), 2)
        if element:
            for index, ele in enumerate(element):
                ele = '='.join(ele)
                element[index] = ele
            element = '&'.join(element)
            self.qd = QueryDict(element, mutable=True)

    def group(self, iterable, count):
        return zip(*[iter(iterable)] * count)


class SeoHelper(object):
    SEOTitle = ''
    SEOKeywords = ''
    SEODescription = ''
    title = ''
    has_data = None

    def __init__(self, model, kwargs):
        self.kwargs = kwargs
        self.model = model
        self.get_attr()
        self.get_seo()

    def get_seo(self):
        if self.kwargs:
            district = self.get_district()
            price = self.get_price()
            self.SEOKeywords = self.SEODescription = '{0} {1} {2}'.format(self.title, district, price)

    def get_district(self):
        district = self.kwargs.get('district', None)
        if district:
            distr = District.objects.get(id=district)
            return distr.name
        return ''

    def get_price(self):
        price__gt = self.kwargs.get('price__gt')
        price__lt = self.kwargs.get('price__lt')
        if price__gt:
            price_gt = 'от {0}'.format(price__gt)
        else:
            price_gt = ''
        if price__lt:
            price_lt = ' до {0}'.format(price__lt)
        else:
            price_lt = ''
        return price_gt+price_lt

    def get_attr(self):
        if self.kwargs:
            td = self.get_type_deal()
            ap = self.get_appointment()
            city = self.get_city()
            self.SEOTitle = self.title = '{0} {1} {2}'.format(td, ap, city)
            self.has_data = True


    def get_type_deal(self):
        type_deal_dict = dict(TypeDeal.CHOICES)
        type_deal = self.kwargs.get('type_deal')
        type_deal_list = self.kwargs.getlist('type_deal')
        if len(type_deal_list) > 1:
            td = '{0} и {1}'.format(type_deal_dict.get(type_deal_list[0]), type_deal_dict.get(type_deal_list[1]))
        else:
            td = type_deal_dict.get(type_deal)
            if not td:
                td = ''
        return td

    def get_appointment(self):
        # appointment
        ap = self.kwargs.get('appointment')
        if ap:
            if hasattr(TypeAppointment, ap.upper()):
                ap_deal_dict = dict(TypeAppointment.CHOICES)
            elif hasattr(TypeAppointmentOffice, ap.upper()):
                ap_deal_dict = dict(TypeAppointmentOffice.CHOICES)
            else:
                ap_deal_dict = {}
            ap = ap_deal_dict.get(ap)
            if ap[-1] == 'а':
                ap = ap[0:-1] + 'ы'
            else:
                ap += 'а'
            return ap.lower()
        return ''

    def get_city(self):
        return SettingsAddress.get_solo().city.strip('.г')

