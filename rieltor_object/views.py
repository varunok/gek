# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from admin2.models import OfisPageModel, BuildingPageModel, DailyPageModel
from common.mixins import ViewsCountMixin, DinamicNextMixin
from rieltor_object.filters import FilterBuilding, FilterOfise, FilterNewBuilding, FilterDaily
from rieltor_object.helpers import HelperFilter
from rieltor_object.mixins import BuildingStatusMixin, OfficeStatusMixin, DailyStatusMixin
from rieltor_object.models import Building, Ofice, NewBuilding, Daily, Earth
from seo.models import SEO

PAGINATE_OBJ = 10


class BuildingListSiteView(BuildingStatusMixin, ListView):
    model = Building
    template_name = 'rieltor_object/building_list.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(BuildingListSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        path = 'http://' + settings.ALLOWED_HOSTS[0] + self.request.get_full_path()
        if SEO.objects.filter(url=path).exists():
            context['seo'] = SEO.objects.filter(url=path).first()
        else:
            context['seo'] = BuildingPageModel.get_solo()
        if queryFilter:
            context['object_list'] = FilterBuilding(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterBuilding(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterBuilding(self.request.GET, queryset=self.object_list)
            context['count_obj'] = Building.objects.count()
        context['BASE_URL'] = '/objects/buildings'
        context['clear_filter'] = reverse_lazy('objects:buildings')
        return context


class BuildingDetailSiteView(BuildingStatusMixin, ViewsCountMixin, DetailView):
    model = Building
    template_name = 'rieltor_object/building.html'


class OficeListSiteView(OfficeStatusMixin, ListView):
    model = Ofice
    template_name = 'rieltor_object/ofice_list.html'
    paginate_by = PAGINATE_OBJ
    
    def get_context_data(self, **kwargs):
        context = super(OficeListSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        path = 'http://' + settings.ALLOWED_HOSTS[0] + self.request.get_full_path()
        if SEO.objects.filter(url=path).exists():
            context['seo'] = SEO.objects.filter(url=path).first()
        else:
            context['seo'] = OfisPageModel.get_solo()
        if queryFilter:
            context['object_list'] = FilterOfise(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterOfise(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterOfise(self.request.GET, queryset=self.object_list)
            context['count_obj'] = Ofice.objects.count()
        context['BASE_URL'] = '/objects/offices'
        context['clear_filter'] = reverse_lazy('objects:ofices')
        return context


class OficeDetailSiteView(OfficeStatusMixin, ViewsCountMixin, DetailView):
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


class DailyListSiteView(DailyStatusMixin, ListView):
    model = Daily
    template_name = 'rieltor_object/daily_list.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(DailyListSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        path = 'http://' + settings.ALLOWED_HOSTS[0] + self.request.get_full_path()
        if SEO.objects.filter(url=path).exists():
            context['seo'] = SEO.objects.filter(url=path).first()
        else:
            context['seo'] = DailyPageModel.get_solo()
        if queryFilter:
            context['object_list'] = FilterDaily(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterDaily(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterDaily(self.request.GET, queryset=self.object_list)
            context['count_obj'] = Ofice.objects.count()
        context['BASE_URL'] = '/objects/dailys'
        context['clear_filter'] = reverse_lazy('objects:dailys')
        return context


class DailyDetailSiteView(DailyStatusMixin, ViewsCountMixin, DetailView):
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