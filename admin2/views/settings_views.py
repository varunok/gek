# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from admin2.forms import SettingFranchiseAddForm
from admin2.mixins import AccesMixin
from admin2.models import Settings, SettingsAddress, SettingsFranchise, ActiveFranchise, SettingsPrivate24, \
    SettingsLiqpay
from common.mixins import MessageMixin


class SettingsCurrencyView(AccesMixin, MessageMixin, UpdateView):
    model = Settings
    template_name = 'admin2/settings/settings_currency.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings')

    def get_object(self, queryset=None):
        return Settings.get_solo()


class SettingsSite(AccesMixin, MessageMixin, UpdateView):
    model = Site
    template_name = 'admin2/settings/settings_site.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings_site')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=1)


class SettingsAddressView(AccesMixin, MessageMixin, UpdateView):
    model = SettingsAddress
    template_name = 'admin2/settings/settings_address.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings_address')

    def get_object(self, queryset=None):
        return SettingsAddress.get_solo()


class SettingFranchise(AccesMixin, MessageMixin, UpdateView):
    model = SettingsFranchise
    template_name = 'admin2/settings/settings_franchise.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings_franchise')

    def get_object(self, queryset=None):
        return SettingsFranchise.get_solo()


class SettingFranchiseAdd(AccesMixin, MessageMixin, UpdateView):
    model = ActiveFranchise
    template_name = 'admin2/settings/settings_franchise_add.html'
    success_url = reverse_lazy('admin2:settings_franchise_add')
    form_class = SettingFranchiseAddForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(self.success_url)
        return super(SettingFranchiseAdd, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return ActiveFranchise.get_solo()


class SettingsPrivate24View(AccesMixin, MessageMixin, UpdateView):
    model = SettingsPrivate24
    template_name = 'admin2/settings/settings_private24.html'
    success_url = reverse_lazy('admin2:settings_private24')
    fields = '__all__'

    def get_object(self, queryset=None):
        return SettingsPrivate24.get_solo()


class SettingsLiqpayView(AccesMixin, MessageMixin, UpdateView):
    model = SettingsLiqpay
    template_name = 'admin2/settings/settings_liqpay.html'
    success_url = reverse_lazy('admin2:settings_liqpay')
    fields = '__all__'

    def get_object(self, queryset=None):
        return SettingsLiqpay.get_solo()


