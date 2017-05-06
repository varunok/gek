# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from rieltor_object.filters import FilterBuilding, FilterOfise
from rieltor_object.models import Building, Ofice
from rieltor_object.views import BuildingListSiteView, BuildingDetailSiteView, \
    OficeDetailSiteView, OficeListSiteView, NewBuildingListSiteView, NewBuildingDetailSiteView, DailyListSiteView, \
    DailyDetailSiteView, EarthSiteView

urlpatterns = [
    # building

    url('^detail/buildings/(?P<pk>[\w-]+)/$', BuildingDetailSiteView.as_view(), name='buildings_detail'),
    url('^buildings/[\w-]*', BuildingListSiteView.as_view(), name='buildings'),

    # newbuilding
    url('^newbuildings/$', NewBuildingListSiteView.as_view(), name='newbuildings'),
    url('^newbuildings/(?P<slug>[\w-]+)$', NewBuildingDetailSiteView.as_view(), name='newbuilding_detail'),

    # ofices
    url('^offices/[\w-]*', OficeListSiteView.as_view(), name='ofices'),
    url('^detail/offices/(?P<pk>[\w-]+)/$', OficeDetailSiteView.as_view(), name='ofice_detail'),

    # daily
    url('^dailys/$', DailyListSiteView.as_view(), name='dailys'),
    url('^dailys/(?P<pk>[\w-]+)/$', DailyDetailSiteView.as_view(), name='daily_detail'),

    # earth
    url('^earth/$', EarthSiteView.as_view(), name='earth'),
    # url('^earth/(?P<pk>[\w-]+)/$', DailyDetailSiteView.as_view(), name='earth_detail'),
]

