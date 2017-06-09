# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import FieldError


class BuildingFilterClass(object):
    qs = None

    def __init__(self, request, model):
        self.request = request
        self.model = model
        if hasattr(model, 'point'):
            self.qs = model.objects.order_by('point')
        else:
            self.qs = model.objects.order_by('custom_id')
        self.get_qs()

    def get_qs(self):
        for search in self.request.GET:
            attr = search.split('__')[0]
            if hasattr(self.model, attr) and self.request.GET.get(search):
                try:
                    self.qs = self.qs.filter(**{search: self.request.GET.get(search)})
                except:
                    pass
            elif attr == 'status':
                status = self.request.GET.get(search)
                if status == 'vip':
                    self.qs = self.qs.filter(**{'is_vip': True})
                if status == 'short':
                    self.qs = self.qs.filter(**{'is_short': True})
                if status == 'default':
                    self.qs = self.qs.filter(**{'is_short': False, 'is_vip': False})