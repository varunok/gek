# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import VideoServiceSet, OficeEditForm
from admin2.helpers import BuildingFilterClass
from admin2.mixins import OfficesStatusMixin
from common.mixins import DeleteAjaxMixin, SuccesMixin, MessageMixin
from rieltor_object.models import Ofice


class OficeListView(OfficesStatusMixin, ListView):
    model = Ofice
    template_name = 'admin2/rieltor_object/ofice/ofice_list.html'
    paginate_by = 10
    ordering = ['point']

    def get_queryset(self):
        qs = self.model.objects.order_by('point')
        if self.request.GET.get('search') == 'Поиск':
            qs = BuildingFilterClass(self.request, self.model).qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(OficeListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Офисы и магазины'
        context['create_url'] = reverse_lazy('admin2:ofice_create')
        return context


class OficeEditView(SuccesMixin, MessageMixin, OfficesStatusMixin, UpdateView):
    model = Ofice
    template_name = 'admin2/rieltor_object/ofice/ofice_edit.html'
    form_class = OficeEditForm

    def get_context_data(self, **kwargs):
        context = super(OficeEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['verbose_name'] = self.model._meta.verbose_name
        return context


class OficeCreateView(SuccesMixin, MessageMixin, OfficesStatusMixin, CreateView):
    model = Ofice
    form_class = OficeEditForm
    template_name = 'admin2/rieltor_object/ofice/ofice_edit.html'


    def get_context_data(self, **kwargs):
        context = super(OficeCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:ofices')
        return context


class OficeDeleteView(OfficesStatusMixin, LoginRequiredMixin, DeleteView):
    model = Ofice
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:ofices')