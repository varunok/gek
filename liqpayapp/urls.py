# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from liqpayapp.views import ConfirmLiqpay
from privat24.views import PayList, ConfirmPayPrivat24

urlpatterns = [
    # liqpay
    url('^$', PayList.as_view(), name='paylist'),
    url('^confirm$', ConfirmLiqpay.as_view(), name='pay_confirm'),
]