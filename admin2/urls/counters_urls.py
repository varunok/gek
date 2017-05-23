# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.counters_views import CounterView

urlpatterns = [
    # COUNTERS
    url(
        '^counter/$',
        CounterView.as_view(),
        name='counter'
    ),
]