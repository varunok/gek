# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import services_views

urlpatterns = [
    # SERVICES
    url(
        r'^services/$',
        services_views.ServicesView.as_view(),
        name='services'
    ),
    url(
        r'status_service',
        services_views.status_service,
        name='status_service'
    ),
    url(
        r'^services/edit/rieltor_service/$',
        services_views.RieltorServiceView.as_view(),
        name='rieltor_service_edit'
    ),
    url(
        r'^services/edit/valuation/$',
        services_views.ValuationServiceView.as_view(),
        name='valuation_edit'
    ),
    url(
        r'^services/edit/repair/$',
        services_views.RepairServiceView.as_view(),
        name='repair_edit'
    ),
    url(
        r'^services/edit/insurence/$',
        services_views.InsurenceServiceView.as_view(),
        name='insurence_edit'
    ),
    url(
        r'^services/edit/cleaning/$',
        services_views.CleaningServiceView.as_view(),
        name='cleaning_edit'
    ),
    url(
        r'^services/edit/installation_water/$',
        services_views.InstallationWaterServiceView.as_view(),
        name='installation_water_edit'
    ),
    url(
        r'^services/edit/universal/(?P<pk>[\w-]+)/$',
        services_views.UniversalServiceView.as_view(),
        name='universal_edit'
    ),
    url(
        r'^services/create/universal/$',
        services_views.UniversalServiceCreate.as_view(),
        name='universal_create'
    ),
    url(
        '^services/delete/(?P<slug>[\w-]+)/$',
        services_views.UniversalServiceDeleteView.as_view(),
        name='sections_delete'
    ),
]