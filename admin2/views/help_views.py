# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.models import Help
from common.mixins import MessageMixin


class HelpWatchView(LoginRequiredMixin, ListView):
    model = Help
    template_name = 'admin2/helps/help_watch.html'

    def get_queryset(self):
        return self.model.objects.is_enable()


class HelpListEditView(LoginRequiredMixin, ListView):
    model = Help
    template_name = 'admin2/helps/help_list.html'


class HelpEdit(LoginRequiredMixin, MessageMixin, UpdateView):
    model = Help
    template_name = 'admin2/helps/help_edit.html'
    pk_url_kwarg = 'pk'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin2:help_edit', args=[self.object.id])


class HelpCreate(LoginRequiredMixin, MessageMixin, CreateView):
    model = Help
    template_name = 'admin2/helps/help_edit.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin2:help_edit', args=[self.object.id])


class HelpDelete(LoginRequiredMixin, DeleteView):
    model = Help
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'

    def get_success_url(self):
        return reverse_lazy('admin2:helps_list')

