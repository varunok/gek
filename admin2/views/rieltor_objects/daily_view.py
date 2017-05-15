# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import VideoServiceSet, DailyEditForm
from admin2.mixins import DailyStatusMixin
from common.mixins import DeleteAjaxMixin, SuccesMixin, MessageMixin
from rieltor_object.models import Daily, Infrastructure


class DailyListView(DailyStatusMixin, ListView):
    model = Daily
    template_name = 'admin2/rieltor_object/daily/daily_list.html'
    paginate_by = 10
    ordering = ['point']

    def get_context_data(self, **kwargs):
        context = super(DailyListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Посуточно'
        context['create_url'] = reverse_lazy('admin2:daily_create')
        return context


class DailyEditView(SuccesMixin, MessageMixin, DailyStatusMixin, UpdateView):
    model = Daily
    template_name = 'admin2/rieltor_object/daily/daily_edit.html'
    form_class = DailyEditForm
    video_form = VideoServiceSet

    def get_context_data(self, **kwargs):
        context = super(DailyEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['video_form'] = self.video_form(instance=self.get_object())
        context['video_check'] = self.get_object().videos.all().order_by('id')
        context['verbose_name'] = self.model._meta.verbose_name
        context['infrastructures'] = Infrastructure.objects.exclude(daily=self.object)
        return context


class DailyCreateView(SuccesMixin, MessageMixin, DailyStatusMixin, CreateView):
    model = Daily
    form_class = DailyEditForm
    template_name = 'admin2/rieltor_object/daily/daily_edit.html'


    def get_context_data(self, **kwargs):
        context = super(DailyCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:dailys')
        return context


class DailyDeleteView(LoginRequiredMixin, DeleteView):
    model = Daily
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:dailys')