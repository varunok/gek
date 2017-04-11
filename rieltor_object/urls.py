# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from rieltor_object.views import BuildingListSiteView, BuildingDetailSiteView, searchbuildingview, SearchBuildView

urlpatterns = [
    # building
    url('^buildings/$', BuildingListSiteView.as_view(), name='buildings'),
    url('^buildings/(?P<pk>[\w-]+)/$', BuildingDetailSiteView.as_view(), name='buildings_detail'),

]
urlpatterns_search = [
    url(r'search_building/$', SearchBuildView.as_view(), name='buildings_search'),
]