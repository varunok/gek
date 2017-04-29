# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from admin2.views.rieltor_objects.building_view import BuildingListView, BuildingEditView, BuildingCreateView, \
    BuildingDeleteView
from admin2.views.rieltor_objects.daily_view import DailyListView, DailyEditView, DailyCreateView, DailyDeleteView
from admin2.views.rieltor_objects.earth_view import EarthListView, EarthEditView, EarthCreateView, EarthDeleteView
from admin2.views.rieltor_objects.newbuilding_view import NewBuildingListView, NewBuildingEditView, \
    NewBuildingCreateView, NewBuildingDeleteView
from admin2.views.rieltor_objects.ofice_view import OficeListView, OficeEditView, OficeCreateView, OficeDeleteView

urlpatterns = [
    # building
    url('^objects/buildings/$', BuildingListView.as_view(), name='buildings'),
    url('^objects/buildings/edit/(?P<pk>[\w-]+)/$', BuildingEditView.as_view(), name='building_edit'),
    url('^objects/buildings/create/$', BuildingCreateView.as_view(), name='building_create'),
    url('^objects/buildings/delete/(?P<pk>[\w-]+)/$', BuildingDeleteView.as_view(),name='building_delete'),

    # ofice
    url('^objects/ofices/$', OficeListView.as_view(), name='ofices'),
    url('^objects/ofices/edit/(?P<pk>[\w-]+)/$', OficeEditView.as_view(), name='ofice_edit'),
    url('^objects/ofices/create/$', OficeCreateView.as_view(), name='ofice_create'),
    url('^objects/ofices/delete/(?P<pk>[\w-]+)/$', OficeDeleteView.as_view(),name='ofice_delete'),

    # newbuilding
    url('^objects/newbuilding/$', NewBuildingListView.as_view(), name='newbuildings'),
    url('^objects/newbuilding/edit/(?P<pk>[\w-]+)/$', NewBuildingEditView.as_view(), name='newbuilding_edit'),
    url('^objects/newbuilding/create/$', NewBuildingCreateView.as_view(), name='newbuilding_create'),
    url('^objects/newbuilding/delete/(?P<pk>[\w-]+)/$', NewBuildingDeleteView.as_view(),name='newbuilding_delete'),

    # daily
    url('^objects/daily/$', DailyListView.as_view(), name='dailys'),
    url('^objects/daily/edit/(?P<pk>[\w-]+)/$', DailyEditView.as_view(), name='daily_edit'),
    url('^objects/daily/create/$', DailyCreateView.as_view(), name='daily_create'),
    url('^objects/daily/delete/(?P<pk>[\w-]+)/$', DailyDeleteView.as_view(),name='daily_delete'),

    # earth
    url('^objects/earth/$', EarthListView.as_view(), name='earth'),
    url('^objects/earth/edit/(?P<pk>[\w-]+)/$', EarthEditView.as_view(), name='earth_edit'),
    url('^objects/earth/create/$', EarthCreateView.as_view(), name='earth_create'),
    url('^objects/earth/delete/(?P<pk>[\w-]+)/$', EarthDeleteView.as_view(),name='earth_delete'),


]