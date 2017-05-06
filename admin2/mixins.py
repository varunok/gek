# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from admin2.models import BuildingPageModel, OfisPageModel


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