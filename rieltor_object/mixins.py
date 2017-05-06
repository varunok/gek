# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect

from admin2.models import BuildingPageModel, OfisPageModel, DailyPageModel


class BuildingStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not BuildingPageModel.get_solo().is_enable:
            return HttpResponseRedirect('/')
        return super(BuildingStatusMixin, self).get(request, *args, **kwargs)


class OfficeStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not OfisPageModel.get_solo().is_enable:
            return HttpResponseRedirect('/')
        return super(OfficeStatusMixin, self).get(request, *args, **kwargs)


class DailyStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not DailyPageModel.get_solo().is_enable:
            return HttpResponseRedirect('/')
        return super(DailyStatusMixin, self).get(request, *args, **kwargs)