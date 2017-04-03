# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from services.views import ServicesSiteView, RieltorServiceView, ValuationView

urlpatterns = [
    url('^$', ServicesSiteView.as_view(), name='services'),
    url('^(?P<slug>[\w-]+)/$', RieltorServiceView.as_view(), name='rieltor_service'),
    url('^valuation/(?P<slug>[\w-]+)/$', ValuationView.as_view(), name='valuation'),
    ]