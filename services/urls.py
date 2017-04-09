# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from services.views import ServicesSiteView, RieltorServiceView, ValuationView, RepairView, InsuranceView, \
    CleaningView, InstallationWaterView, UniversalView

urlpatterns = [
    url('^$', ServicesSiteView.as_view(), name='services'),
    url('^(?P<slug>[\w-]+)/$', RieltorServiceView.as_view(), name='rieltor_service'),
    url('^valuation/(?P<slug>[\w-]+)/$', ValuationView.as_view(), name='valuation'),
    url('^repair/(?P<slug>[\w-]+)/$', RepairView.as_view(), name='repair'),
    url('^insurance/(?P<slug>[\w-]+)/$', InsuranceView.as_view(), name='insurance'),
    url('^cleaning/(?P<slug>[\w-]+)/$', CleaningView.as_view(), name='cleaning'),
    url('^installation_water/(?P<slug>[\w-]+)/$', InstallationWaterView.as_view(), name='installation_water'),
    url('^universal/(?P<slug>[\w-]+)/$', UniversalView.as_view(), name='universal'),
]
