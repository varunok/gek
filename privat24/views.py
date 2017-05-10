# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, FormView, TemplateView

from admin2.models import SettingsFranchise, SettingsPrivate24, ActiveFranchise
from privat24.forms import PayListForm, Privat24TransactionForm
from hashlib import md5, sha1
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import QueryDict
from django.utils.crypto import get_random_string

from privat24.models import Privat24Transaction, OrderCounter


class PayList(UpdateView):
    template_name = 'privat24/pay_list.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PayList, self).get_context_data(**kwargs)
        context['currency'] = SettingsPrivate24.get_solo().currency
        return context


    def get_object(self, queryset=None):
        return SettingsFranchise.get_solo()


class ConfirmPayPrivat24(TemplateView):
    template_name = 'privat24/pay_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmPayPrivat24, self).get_context_data(**kwargs)
        days = self.kwargs.get('days')
        context['privat_setting'] = SettingsPrivate24.get_solo()
        context['price'] = getattr(SettingsFranchise.get_solo(), 'price_{0}'.format(days))
        context['days'] = days
        context['method'] = 'Приват24'
        site = Site.objects.get_current().domain
        return_url = site + str(reverse_lazy('privat24:pay_done'))
        server_url = site + str(reverse_lazy('privat24:pay_callback'))
        sid = unique_id = get_random_string(length=16)
        order = OrderCounter.get_solo()
        order.counter = order.counter + 1
        order.save()
        fields = {
            'sid': sid,
            'amt': context['price'],
            'ccy': context['privat_setting'].currency,
            'merchant': context['privat_setting'].merchant,
            'order': order.counter,
            'details': 'Продление франшизы',
            'ext_details': 'Дней %s' % days,
            'pay_way': 'privat24',
            'return_url': return_url,
            'server_url': server_url,
            'signature': context['privat_setting'].signature
        }
        context['fields'] = fields
        return context


@csrf_exempt
def PayDone(request):
    template_name = 'privat24/pay_done.html'
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