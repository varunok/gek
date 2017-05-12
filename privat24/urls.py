# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from privat24.views import ConfirmPayPrivat24, pay_callback, PayDone

urlpatterns = [
    # privat24
    url('^confirm/(?P<days>[\w-]+)/$', ConfirmPayPrivat24.as_view(), name='pay_confirm'),
    url('^api/callback$', pay_callback, name='callback_p24'),
    url('^pay_done$', PayDone, name='done_p24'),
]