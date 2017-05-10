# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from privat24.views import PayList, ConfirmPayPrivat24, pay_callback, PayDone

urlpatterns = [
    # privat24
    url('^$', PayList.as_view(), name='paylist'),
    url('^confirm/(?P<days>[\w-]+)/$', ConfirmPayPrivat24.as_view(), name='pay_confirm'),
    url('^api/callback$', pay_callback, name='pay_callback'),
    url('^pay_done$', PayDone, name='pay_done'),
]