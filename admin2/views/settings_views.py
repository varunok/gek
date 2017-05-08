# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from admin2.models import Settings, SettingsAddress
from common.mixins import MessageMixin


class SettingsCurrencyView(MessageMixin, UpdateView):
    model = Settings
    template_name = 'admin2/settings/settings_currency.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings')

    def get_object(self, queryset=None):
        return Settings.get_solo()



class SettingsSite(UpdateView):
    model = Site
    template_name = 'admin2/settings/settings_site.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings_site')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=1)


class SettingsAddressView(UpdateView):
    model = SettingsAddress
    template_name = 'admin2/settings/settings_address.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings_address')

    def get_object(self, queryset=None):
        return SettingsAddress.get_solo()
