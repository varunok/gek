# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView, FormView, TemplateView

from common.mixins import ViewsCountMixin, DinamicNextMixin
from rieltor_object.models import Building, TypeDeal, Ofice, NewBuilding, Daily, Earth
from rieltor_object.filters import FilterBuilding, FilterOfise, FilterNewBuilding

PAGINATE_OBJ = 10

class BuildingListSiteView(DinamicNextMixin, ListView):
    model = Building
    template_name = 'rieltor_object/building_list.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(BuildingListSiteView, self).get_context_data(**kwargs)
        context['filter_form'] = FilterBuilding(self.request.GET, queryset=self.model.objects.all())
        context['url_action'] = reverse_lazy('buildings_search')
        return context


class BuildingDetailSiteView(ViewsCountMixin, DetailView):
    model = Building
    template_name = 'rieltor_object/building.html'


class FilterBuildOficeView(DinamicNextMixin, ListView):
    paginate_by = PAGINATE_OBJ
    template_name = 'rieltor_object/include/building_item.html'
    dinamic_template_name = 'rieltor_object/include/building_item.html'

    def get_queryset(self):
        filterset = self.kwargs.get('filterset')
        return filterset(self.request.POST, queryset=self.model.objects.all()).qs


class OficeListSiteView(DinamicNextMixin, ListView):
    model = Ofice
    template_name = 'rieltor_object/ofice_list.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(OficeListSiteView, self).get_context_data(**kwargs)
        context['filter_form'] = FilterOfise(self.request.GET, queryset=self.model.objects.all())
        context['url_action'] = reverse_lazy('ofices_search')
        return context


class OficeDetailSiteView(ViewsCountMixin, DetailView):
    model = Ofice
    template_name = 'rieltor_object/ofice.html'


class NewBuildingListSiteView(DinamicNextMixin, ListView):
    model = NewBuilding
    template_name = 'rieltor_object/newbuilding_list.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(NewBuildingListSiteView, self).get_context_data(**kwargs)
        context['filter_form'] = FilterNewBuilding(self.request.GET, queryset=self.model.objects.all())
        return context


class NewBuildingDetailSiteView(ViewsCountMixin, DetailView):
    model = NewBuilding
    template_name = 'rieltor_object/newbuilding.html'


class DailyListSiteView(DinamicNextMixin, ListView):
    model = Daily
    template_name = 'rieltor_object/daily_list.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(DailyListSiteView, self).get_context_data(**kwargs)
        # context['filter_form'] = FilterNewBuilding(self.request.GET, queryset=self.model.objects.all())
        return context


class DailyDetailSiteView(ViewsCountMixin, DetailView):
    model = Daily
    template_name = 'rieltor_object/daily.html'


class EarthSiteView(DinamicNextMixin, ListView):
    model = Earth
    template_name = 'rieltor_object/earth.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(EarthSiteView, self).get_context_data(**kwargs)
        # context['filter_form'] = FilterNewBuilding(self.request.GET, queryset=self.model.objects.all())
        return context