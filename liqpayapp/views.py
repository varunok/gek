# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from liqpay.liqpay import LiqPay
# Create your views here.


class ConfirmLiqpay(TemplateView):
    template_name = 'privat24/pay_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmLiqpay, self).get_context_data(**kwargs)
        liqpay = LiqPay('i8041022806', 'fseocB1BSvg1wHDXVoHblE2AWZHSVOZfg4RBo5HUedj2d5')
        context['html'] = liqpay.cnb_form({
            "action": "pay",
            "amount": "1",
            "currency": "USD",
            "description": "description text",
            "order_id": "order_id_1",
            "version": "3",
            "server_url": 'http://varunok.ddns.net/p24/api/callback',
            'result_url': 'http://varunok.ddns.net',
        })
        return context

