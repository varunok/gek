# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import json

import datetime
from django.contrib.sites.models import Site
from django.http import QueryDict, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from liqpay.liqpay import LiqPay
# Create your views here.
from admin2.models import SettingsFranchise, SettingsLiqpay, ActiveFranchise
from liqpayapp.forms import LiqPayTransactionForm
from privat24.models import OrderCounter


class ConfirmLiqpay(TemplateView):
    template_name = 'admin2/pay/pay_confirm.html'
    public_key = None

    def get_context_data(self, **kwargs):
        context = super(ConfirmLiqpay, self).get_context_data(**kwargs)
        days = self.kwargs.get('days')
        context['price'] = getattr(SettingsFranchise.get_solo(), 'price_{0}'.format(days))
        context['currency'] = SettingsFranchise.get_solo().currency
        context['method'] = 'LiqPay'
        context['title'] = 'Оплата через LiqPay'
        site = Site.objects.get_current()
        liqpay = LiqPay(get_liqpay_public_key(), get_liqpay_signature())
        result_url = site.domain + str(reverse_lazy('liqpay:done_liqpay'))
        server_url = site.domain + str(reverse_lazy('liqpay:callback_liqpay'))
        context['html'] = liqpay.cnb_form({
            "action": "pay",
            "amount": context['price'],
            "currency": context['currency'],
            "description": "Продление франшизы " + site.name,
            "order_id": self.get_order_count(),
            "version": "3",
            # "sandbox": "yes",
            "server_url": server_url,
            'result_url': result_url,
            'info': days,
        })

        return context



    def get_order_count(self):
        site = Site.objects.get_current().name
        order = OrderCounter.get_solo()
        order.counter = order.counter + 1
        order.save()
        order_text = site + str(order.counter)
        return order_text.upper()


def get_liqpay_public_key():
    return SettingsLiqpay.get_solo().merchant

def get_liqpay_signature():
   return SettingsLiqpay.get_solo().signature


@csrf_exempt
def PayDone(request):
    template_name = 'admin2/pay/pay_done.html'
    try:
        payment = QueryDict(request.POST.get('payment').encode('utf-8'))
    except:
        payment = {'state':'ok'}
    if payment['state'] in ['ok', 'test']:
        state = 'Оплата завершена'
    else:
        state = 'Оплата Error'
    return render(request, template_name, {'state':state})


@csrf_exempt
def pay_callback(request):
    liqpay = LiqPay(get_liqpay_public_key(), get_liqpay_signature())
    data = request.POST.get('data')
    signature = request.POST.get('signature')
    sign = liqpay.str_to_sign(
        get_liqpay_signature() + data + get_liqpay_signature()
    )
    if sign == str(signature):
        qdict = QueryDict('', mutable=True)
        qdict.update(json.loads(base64.b64decode(data)))
        form = LiqPayTransactionForm(qdict)
        if form.is_valid():
            form.save()
            day = qdict.get('info')
            if isinstance(day, unicode):
                day = int(day)
            active_franchise = ActiveFranchise.get_solo()
            active_franchise.active_franchise += datetime.timedelta(days=day)
            active_franchise.save()
        else:
            print(form.errors)
        return HttpResponse(status=200)
    return HttpResponse(status=500)

