# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from services.views import ServicesSiteView, RieltorServiceView

urlpatterns = [
    url('^$', ServicesSiteView.as_view(), name='services'),
    url('^rieltor-service$', RieltorServiceView.as_view(), name='rieltor_service'),
    ]