# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.pay_views import PayList

urlpatterns = [
    # privat24
    url('^paylist$', PayList.as_view(), name='paylist'),
]