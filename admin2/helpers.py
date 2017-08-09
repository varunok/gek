# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
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
            if attr == u'when_create':
                when_create = self.request.GET.get(search)
                when_create__gte, when_create__lte = when_create.split('-')
                when_create__gte = when_create__gte.strip(' ')
                when_create__lte = when_create__lte.strip(' ')
                when_create__gte = datetime.strptime(when_create__gte, '%d.%m.%Y')
                when_create__lte = datetime.strptime(when_create__lte, '%d.%m.%Y')
                self.qs = self.qs.filter(
                    **{'when_create__date__gte': when_create__gte})
                self.qs = self.qs.filter(
                    **{'when_create__date__lte': when_create__lte})