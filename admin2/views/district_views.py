# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from admin2.mixins import DistrictQueryMixin, DistrictContextMixin
from rieltor_object.models import District, DailyDistrict, EarthDistrict


class DistrictsNav(TemplateView):
    template_name = 'admin2/districts/district_nav.html'

    def get_context_data(self, **kwargs):
        context = super(DistrictsNav, self).get_context_data(**kwargs)
        context['District'] = District.__name__
        context['DailyDistrict'] = DailyDistrict.__name__
        context['EarthDistrict'] = EarthDistrict.__name__
        return context


class DistrictListView(DistrictQueryMixin, DistrictContextMixin, ListView):
    # model = District
    template_name = 'admin2/districts/district_list.html'
    paginate_by = 10
    is_list_view = True


class DistrictCreate(DistrictQueryMixin, DistrictContextMixin, CreateView):
    # model = District
    template_name = 'admin2/districts/district_edit.html'
    fields = '__all__'


class DistrictEdit(DistrictQueryMixin, DistrictContextMixin, UpdateView):
    # model = District
    template_name = 'admin2/districts/district_edit.html'
    fields = '__all__'


class DistrictDelete(DistrictQueryMixin, DistrictContextMixin, DeleteView):
    # model = District
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
