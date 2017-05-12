# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from hashlib import md5, sha1

from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.http import QueryDict
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from admin2.models import SettingsFranchise, SettingsPrivate24, ActiveFranchise
from privat24.forms import Privat24TransactionForm
from privat24.models import OrderCounter


class ConfirmPayPrivat24(TemplateView):
    template_name = 'admin2/pay/pay_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmPayPrivat24, self).get_context_data(**kwargs)
        days = self.kwargs.get('days')
        context['privat_setting'] = SettingsPrivate24.get_solo()
        context['price'] = getattr(SettingsFranchise.get_solo(), 'price_{0}'.format(days))
        context['currency'] = SettingsFranchise.get_solo().currency
        context['days'] = days
        context['method'] = 'Приват24'
        context['title'] = 'Оплата через Приват24'
        site = Site.objects.get_current().domain
        return_url = site + str(reverse_lazy('privat24:done_p24'))
        server_url = site + str(reverse_lazy('privat24:callback_p24'))
        sid = unique_id = get_random_string(length=16)
        fields = {
            'sid': sid,
            'amt': context['price'],
            'ccy': context['currency'],
            'merchant': context['privat_setting'].merchant,
            'order': self.get_order_count(),
            'details': 'Продление франшизы',
            'ext_details': 'Дней %s' % days,
            'pay_way': 'privat24',
            'return_url': return_url,
            'server_url': server_url,
            'signature': context['privat_setting'].signature
        }
        context['fields'] = fields
        return context

    def get_order_count(self):
        site = Site.objects.get_current().name
        order = OrderCounter.get_solo()
        order.counter = order.counter + 1
        order.save()
        order_text = site + str(order.counter)
        return order_text.upper()


@csrf_exempt
def PayDone(request):
    template_name = 'admin2/pay/pay_done.html'
    payment = QueryDict(request.POST.get('payment').encode('utf-8'))
    if payment['state'] in ['ok', 'test']:
        state = 'Оплата проведена'
    else:
        state = 'Оплата Error'
    return render(request, template_name, {'state':state})


@csrf_exempt
def pay_callback(request):
    payment = QueryDict(request.POST.get('payment').encode('utf-8'))
    signature = request.POST.get('signature')
    test_str = ('%s%s'%(request.POST.get('payment'), SettingsPrivate24.get_solo().signature))
    local_signature = sha1(md5(test_str.encode('utf-8')).hexdigest()).hexdigest()
    if signature == local_signature:
        form = Privat24TransactionForm(payment)
        if form.is_valid():
            form = form.save()
            form.signature = signature
            form.save()
            try:
                day = int(form.ext_details.split(' ')[-1])
            except:
                day = 30
            active_franchise = ActiveFranchise.get_solo()
            active_franchise.active_franchise += datetime.timedelta(days=day)
            active_franchise.save()
            return HttpResponse(200)
    return HttpResponse(404)