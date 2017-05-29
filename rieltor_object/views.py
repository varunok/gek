# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
# Create your views here.
from django.contrib.sites.models import Site
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from admin2.models import OfisPageModel, BuildingPageModel, DailyPageModel, NewBuildingPageModel, EarthPageModel
from common.mixins import ViewsCountMixin, DinamicPageMixin
from rieltor_object.filters import FilterBuilding, FilterOfise, FilterNewBuilding, FilterDaily, FilterEarth
from rieltor_object.helpers import HelperFilter
from rieltor_object.mixins import BuildingStatusMixin, OfficeStatusMixin, DailyStatusMixin, NewBuildingStatusMixin, \
    EarthStatusMixin
from rieltor_object.models import Building, Ofice, NewBuilding, Daily, Earth
from seo.mixins import SEOMixin
from seo.models import SEO

PAGINATE_OBJ = 20


class BuildingListSiteView(DinamicPageMixin, SEOMixin, BuildingStatusMixin, ListView):
    model = Building
    template_name = 'rieltor_object/building_list.html'
    paginate_by = PAGINATE_OBJ
    seo_model = BuildingPageModel
    dinamic_template_name = 'rieltor_object/include/building_item.html'


    def get_context_data(self, **kwargs):
        context = super(BuildingListSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        if queryFilter:
            # context['object_list'] = FilterBuilding(queryFilter, queryset=self.object_list).qs
            # self.object_list = FilterBuilding(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterBuilding(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterBuilding(self.request.GET, queryset=self.object_list)
            context['count_obj'] = Building.objects.count()
        context['BASE_URL'] = '/objects/buildings'
        context['clear_filter'] = reverse_lazy('objects:buildings')
        context['buildingpagemodel'] = self.seo_model.get_solo()
        return context

    def get_queryset(self):
        self.object_list = self.model.objects.order_by('-is_vip', 'point')
        queryFilter = HelperFilter(self.request).qd
        if queryFilter:
            self.object_list = FilterBuilding(queryFilter, queryset=self.object_list).qs
        return self.object_list

    def get_template_names(self):
        if str(Site.objects.get_current()) == 'http://dom-phuket.biz':
            return 'rieltor_object/special/building_list.html'
        return self.template_name


class BuildingDetailSiteView(SEOMixin, BuildingStatusMixin, ViewsCountMixin, DetailView):
    model = Building
    template_name = 'rieltor_object/building.html'

    def get_template_names(self):
        if str(Site.objects.get_current()) == 'http://dom-phuket.biz':
            return 'rieltor_object/special/building.html'
        return self.template_name


class OficeListSiteView(SEOMixin, OfficeStatusMixin, ListView):
    model = Ofice
    template_name = 'rieltor_object/ofice_list.html'
    paginate_by = PAGINATE_OBJ
    seo_model = OfisPageModel
    
    def get_context_data(self, **kwargs):
        context = super(OficeListSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        if queryFilter:
            context['object_list'] = FilterOfise(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterOfise(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterOfise(self.request.GET, queryset=self.object_list)
            context['count_obj'] = Ofice.objects.count()
        context['BASE_URL'] = '/objects/offices'
        context['clear_filter'] = reverse_lazy('objects:ofices')
        context['ofispagemodel'] = self.seo_model.get_solo()
        return context


class OficeDetailSiteView(SEOMixin, OfficeStatusMixin, ViewsCountMixin, DetailView):
    model = Ofice
    template_name = 'rieltor_object/ofice.html'


class NewBuildingListSiteView(SEOMixin, NewBuildingStatusMixin, ListView):
    model = NewBuilding
    template_name = 'rieltor_object/newbuilding_list.html'
    paginate_by = PAGINATE_OBJ
    seo_model = NewBuildingPageModel

    def get_context_data(self, **kwargs):
        context = super(NewBuildingListSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        if queryFilter:
            context['object_list'] = FilterNewBuilding(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterNewBuilding(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterNewBuilding(self.request.GET, queryset=self.object_list)
            context['count_obj'] = NewBuilding.objects.count()
        context['BASE_URL'] = '/objects/newbuildings'
        context['clear_filter'] = reverse_lazy('objects:newbuildings')
        context['newbuildingpagemodel'] = self.seo_model.get_solo()
        # context['filter_form'] = FilterNewBuilding(self.request.GET, queryset=self.model.objects.all())
        return context


class NewBuildingDetailSiteView(SEOMixin, NewBuildingStatusMixin, ViewsCountMixin, DetailView):
    model = NewBuilding
    template_name = 'rieltor_object/newbuilding.html'


class DailyListSiteView(DinamicPageMixin, SEOMixin, DailyStatusMixin, ListView):
    model = Daily
    template_name = 'rieltor_object/daily_list.html'
    paginate_by = 2
    seo_model = DailyPageModel
    dinamic_template_name = 'rieltor_object/include/daily_item.html'

    def get_context_data(self, **kwargs):
        context = super(DailyListSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        if queryFilter:
            # context['object_list'] = FilterDaily(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterDaily(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterDaily(self.request.GET, queryset=self.object_list)
            context['count_obj'] = Daily.objects.count()
        context['BASE_URL'] = '/objects/dailys'
        context['clear_filter'] = reverse_lazy('objects:dailys')
        context['dailypagemodel'] = self.seo_model.get_solo()
        return context

    def get_queryset(self):
        self.object_list = self.model.objects.order_by('point')
        queryFilter = HelperFilter(self.request).qd
        if queryFilter:
            self.object_list = FilterBuilding(queryFilter, queryset=self.object_list).qs
        return self.object_list


class DailyDetailSiteView(SEOMixin, DailyStatusMixin, ViewsCountMixin, DetailView):
    model = Daily
    template_name = 'rieltor_object/daily.html'


class EarthSiteView(SEOMixin, EarthStatusMixin, ListView):
    model = Earth
    template_name = 'rieltor_object/earth.html'
    paginate_by = PAGINATE_OBJ
    seo_model = EarthPageModel

    def get_context_data(self, **kwargs):
        context = super(EarthSiteView, self).get_context_data(**kwargs)
        queryFilter = HelperFilter(self.request).qd
        if queryFilter:
            context['object_list'] = FilterEarth(queryFilter, queryset=self.object_list).qs
            context['filter_form'] = FilterEarth(queryFilter, queryset=self.object_list)
        else:
            context['filter_form'] = FilterEarth(self.request.GET, queryset=self.object_list)
            context['count_obj'] = Earth.objects.count()
        context['BASE_URL'] = '/objects/earth'
        context['clear_filter'] = reverse_lazy('objects:earth')
        context['earthpagemodel'] = self.seo_model.get_solo()
        return context