# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, UpdateView, FormView, TemplateView

from admin2.models import SettingsFranchise, SettingsPrivate24
from privat24.forms import PayListForm
from hashlib import md5, sha1


class PayList(UpdateView):
    template_name = 'privat24/pay_list.html'
    fields = '__all__'


    def get_object(self, queryset=None):
        return SettingsFranchise.get_solo()


class ConfirmPayPrivat24(TemplateView):
    template_name = 'privat24/pay_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmPayPrivat24, self).get_context_data(**kwargs)
        context['pay_setting'] = self.get_object()
        context['privat_setting'] = SettingsPrivate24.get_solo()
        context['signature'] = sha1(md5(SettingsPrivate24.get_solo().signature).hexdigest()).hexdigest()
        context['days'] = 30
        return context

    def get_object(self, queryset=None):
        return SettingsFranchise.get_solo()