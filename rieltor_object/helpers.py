# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import QueryDict


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
