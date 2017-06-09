# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from admin2.models import Counters
from common.mixins import MessageMixin


class CounterView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = Counters
    template_name = 'admin2/counters/counters_edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('admin2:counter')

    def get_object(self, queryset=None):
        return self.model.get_solo()
