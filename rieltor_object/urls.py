# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from rieltor_object.filters import FilterBuilding, FilterOfise
from rieltor_object.models import Building, Ofice
from rieltor_object.views import BuildingListSiteView, BuildingDetailSiteView, FilterBuildOficeView, \
    OficeDetailSiteView, OficeListSiteView, NewBuildingListSiteView, NewBuildingDetailSiteView, DailyListSiteView, \
    DailyDetailSiteView, EarthSiteView

urlpatterns = [
    # building
    url('^buildings/$', BuildingListSiteView.as_view(), name='buildings'),
    url('^buildings/(?P<pk>[\w-]+)/$', BuildingDetailSiteView.as_view(), name='buildings_detail'),

    # newbuilding
    url('^newbuildings/$', NewBuildingListSiteView.as_view(), name='newbuildings'),
    url('^newbuildings/(?P<slug>[\w-]+)$', NewBuildingDetailSiteView.as_view(), name='newbuilding_detail'),

    # ofices
    url('^ofices/$', OficeListSiteView.as_view(), name='ofices'),
    url('^ofices/(?P<pk>[\w-]+)/$', OficeDetailSiteView.as_view(), name='ofice_detail'),

    # daily
    url('^dailys/$', DailyListSiteView.as_view(), name='dailys'),
    url('^dailys/(?P<pk>[\w-]+)/$', DailyDetailSiteView.as_view(), name='daily_detail'),

    # earth
    url('^earth/$', EarthSiteView.as_view(), name='earth'),
    # url('^earth/(?P<pk>[\w-]+)/$', DailyDetailSiteView.as_view(), name='earth_detail'),

]

# FILTERING
urlpatterns_search = [
    url(
        r'search_building/$',
        FilterBuildOficeView.as_view(model=Building),
        kwargs={'filterset': FilterBuilding},
        name='buildings_search'
    ),
    url(
        r'search_ofices/$',
        FilterBuildOficeView.as_view(model=Ofice),
        kwargs={'filterset': FilterOfise},
        name='ofices_search'
    ),
]