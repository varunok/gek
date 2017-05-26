# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.district_views import DistrictsNav, DistrictListView, DistrictCreate, DistrictEdit, DistrictDelete

urlpatterns = [
    # District
    url(
        '^districts_nav/$',
        DistrictsNav.as_view(),
        name='districts_nav'
    ),
    url(
        '^district_list/$',
        DistrictListView.as_view(),
        name='district_list'
    ),
    url(
        '^district/create/$',
        DistrictCreate.as_view(),
        name='district_create'
    ),
    url(
        '^district/edit/(?P<pk>[\d-]+)/$',
        DistrictEdit.as_view(),
        name='district_edit'
    ),
    url(
        '^district/delete/(?P<pk>[\d-]+)/$',
        DistrictDelete.as_view(),
        name='district_delete'
    ),
]