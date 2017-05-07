# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from admin2.models import BuildingPageModel, OfisPageModel, DailyPageModel, NewBuildingPageModel, EarthPageModel


class BuildingStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not BuildingPageModel.get_solo().is_enable:
            return HttpResponseRedirect(reverse_lazy('admin2:main'))
        return super(BuildingStatusMixin, self).get(request, *args, **kwargs)


class OfficesStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not OfisPageModel.get_solo().is_enable:
            return HttpResponseRedirect(reverse_lazy('admin2:main'))
        return super(OfficesStatusMixin, self).get(request, *args, **kwargs)


class DailyStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not DailyPageModel.get_solo().is_enable:
            return HttpResponseRedirect(reverse_lazy('admin2:main'))
        return super(DailyStatusMixin, self).get(request, *args, **kwargs)


class NewBuildingStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not NewBuildingPageModel.get_solo().is_enable:
            return HttpResponseRedirect(reverse_lazy('admin2:main'))
        return super(NewBuildingStatusMixin, self).get(request, *args, **kwargs)


class EarthStatusMixin(object):
    def get(self, request, *args, **kwargs):
        if not EarthPageModel.get_solo().is_enable:
            return HttpResponseRedirect(reverse_lazy('admin2:main'))
        return super(EarthStatusMixin, self).get(request, *args, **kwargs)