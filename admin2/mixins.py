# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, Resolver404
from django.views.generic.base import ContextMixin

from admin2.models import BuildingPageModel, OfisPageModel, DailyPageModel, NewBuildingPageModel, EarthPageModel
from rieltor_object.models import District, DailyDistrict, EarthDistrict


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


class AccesMixin(object):
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('admin2:main'))
        return super(AccesMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('admin2:main'))
        return super(AccesMixin, self).post(request, *args, **kwargs)


class DistrictQueryMixin():
    request = None
    is_list_view = False

    def get_queryset(self, *args, **kwargs):
        model = self.request.GET.get('model')
        if not model:
            model = self.request.POST.get('model')
        if len(model) > 13:
            raise Resolver404()
        model = eval(model)
        self.model = model
        if type(model).__name__ == 'ModelBase':
            if self.is_list_view:
                return model.objects.all()
            return model.objects
        raise Resolver404()


class DistrictContextMixin(ContextMixin):
    model = None

    def get_context_data(self, **kwargs):
        context = super(DistrictContextMixin, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name_plural
        context['model_name'] = self.model.__name__
        context['back'] = self.model.objects.get_list_url()
        return context

    def get_success_url(self):
        return '/admin/district_list/?model={0}'.format(self.model.__name__)