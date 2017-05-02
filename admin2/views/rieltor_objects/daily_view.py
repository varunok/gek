# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import VideoServiceSet, DailyEditForm
from common.mixins import DeleteAjaxMixin
from rieltor_object.models import Daily, Infrastructure


class DailyListView(ListView):
    model = Daily
    template_name = 'admin2/rieltor_object/daily/daily_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DailyListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Посуточно'
        context['create_url'] = reverse_lazy('admin2:daily_create')
        return context


class DailyEditView(UpdateView):
    model = Daily
    template_name = 'admin2/rieltor_object/daily/daily_edit.html'
    success_url = reverse_lazy('admin2:dailys')
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


class DailyCreateView(CreateView):
    model = Daily
    form_class = DailyEditForm
    template_name = 'admin2/rieltor_object/daily/daily_edit.html'


    def get_context_data(self, **kwargs):
        context = super(DailyCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:dailys')
        return context

    def get_success_url(self):
        return self.object.get_edit_url()


class DailyDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Daily
    pk_url_kwarg = 'pk'