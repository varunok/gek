# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from liqpayapp.views import ConfirmLiqpay, PayDone, pay_callback

urlpatterns = [
    # liqpay
    url('^confirm/(?P<days>[\w-]+)/$', ConfirmLiqpay.as_view(), name='pay_confirm'),
    url('^api/callback$', pay_callback, name='callback_liqpay'),
    url('^pay_done$', PayDone, name='done_liqpay'),
]