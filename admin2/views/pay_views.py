# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from admin2.models import SettingsPrivate24, SettingsFranchise


class PayList(LoginRequiredMixin, UpdateView):
    template_name = 'admin2/pay/pay_list.html'
    fields = '__all__'

    def get_object(self, queryset=None):
        return SettingsFranchise.get_solo()