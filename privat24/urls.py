# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from privat24.views import PayList, ConfirmPayPrivat24

urlpatterns = [
    # privat24
    url('^$', PayList.as_view(), name='paylist'),
    url('^confirm$', ConfirmPayPrivat24.as_view(), name='pay_confirm'),
]