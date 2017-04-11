# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.rieltor_objects.building_view import BuildingListView, BuildingEditView, BuildingCreateView

urlpatterns = [
    # building
    url('^objects/buildings/$', BuildingListView.as_view(), name='buildings'),
    url('^objects/buildings/edit/(?P<pk>[\w-]+)/$', BuildingEditView.as_view(), name='building_edit'),
    url('^objects/buildings/create/$', BuildingCreateView.as_view(), name='building_create'),

]