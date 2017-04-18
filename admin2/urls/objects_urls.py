# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.rieltor_objects.building_view import BuildingListView, BuildingEditView, BuildingCreateView, \
    BuildingDeleteView
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

]