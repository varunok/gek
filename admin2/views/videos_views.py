# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import WhatYouKnownSet, VideosCreateForm
from common.mixins import FormSetMixin, DeleteAjaxMixin, SuccesMixin, MessageMixin
from videos.models import Videos


class VideosList(ListView):
    template_name = 'admin2/videos/videos_list.html'
    model = Videos
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(VideosList, self).get_context_data(**kwargs)
        context['page_title'] = self.model._meta.verbose_name
        context['create_url'] = reverse_lazy('admin2:videos_create')
        return context


class VideosEdit(SuccesMixin, MessageMixin, UpdateView):
    model = Videos
    form_class = VideosCreateForm
    pk_url_kwarg = 'pk'
    template_name = 'admin2/videos/videos_edit.html'

    def get_context_data(self, **kwargs):
        context = super(VideosEdit, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        return context


class VideosCreate(SuccesMixin, MessageMixin, CreateView):
    model = Videos
    template_name = 'admin2/videos/videos_edit.html'
    form_class = VideosCreateForm

    def get_context_data(self, **kwargs):
        context = super(VideosCreate, self).get_context_data(**kwargs)
        context['list_url'] = reverse_lazy('admin2:videos')
        return context


class VideosKnowsEdit(FormSetMixin):
    model = Videos
    fields = '__all__'
    pk_url_kwarg = 'pk'
    template_name = 'admin2/videos/videos_knows.html'
    formset = WhatYouKnownSet

    def get_success_url(self):
        return reverse_lazy('admin2:videos_edit_knows', args=[self.get_object().id])

    def get_context_data(self, **kwargs):
        context = super(VideosKnowsEdit, self).get_context_data(**kwargs)
        context['page_title'] = self.model._meta.verbose_name
        context['object'] = self.get_object()
        return context


class VideosDeleteView(LoginRequiredMixin, DeleteView):
    model = Videos
    slug_field = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:videos')