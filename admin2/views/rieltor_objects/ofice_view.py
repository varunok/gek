# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import VideoServiceSet, OficeEditForm
from common.mixins import DeleteAjaxMixin
from rieltor_object.models import Ofice


class OficeListView(ListView):
    model = Ofice
    template_name = 'admin2/rieltor_object/building/building_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(OficeListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Офисы и магазины'
        context['create_url'] = reverse_lazy('admin2:ofice_create')
        return context


class OficeEditView(UpdateView):
    model = Ofice
    template_name = 'admin2/rieltor_object/ofice/ofice_edit.html'
    success_url = reverse_lazy('admin2:ofices')
    form_class = OficeEditForm
    video_form = VideoServiceSet

    def get_context_data(self, **kwargs):
        context = super(OficeEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['video_form'] = self.video_form(instance=self.get_object())
        context['video_check'] = self.get_object().videos.all().order_by('id')
        context['verbose_name'] = self.model._meta.verbose_name
        return context


class OficeCreateView(CreateView):
    model = Ofice
    form_class = OficeEditForm
    template_name = 'admin2/rieltor_object/ofice/ofice_edit.html'


    def get_context_data(self, **kwargs):
        context = super(OficeCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:ofices')
        return context

    def get_success_url(self):
        return self.object.get_edit_url()


class OficeDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Ofice
    pk_url_kwarg = 'pk'