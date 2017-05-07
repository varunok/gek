# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import EarthEditForm
from admin2.mixins import EarthStatusMixin
from common.mixins import DeleteAjaxMixin
from rieltor_object.models import Earth


class EarthListView(EarthStatusMixin, ListView):
    model = Earth
    template_name = 'admin2/rieltor_object/earth/earth_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(EarthListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Земля'
        context['create_url'] = reverse_lazy('admin2:earth_create')
        return context


class EarthEditView(EarthStatusMixin, UpdateView):
    model = Earth
    template_name = 'admin2/rieltor_object/earth/earth_edit.html'
    success_url = reverse_lazy('admin2:earth')
    form_class = EarthEditForm


    def get_context_data(self, **kwargs):
        context = super(EarthEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['verbose_name'] = self.model._meta.verbose_name
        return context


class EarthCreateView(EarthStatusMixin, CreateView):
    model = Earth
    form_class = EarthEditForm
    template_name = 'admin2/rieltor_object/earth/earth_edit.html'


    def get_context_data(self, **kwargs):
        context = super(EarthCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:earth')
        return context

    def get_success_url(self):
        return self.object.get_edit_url()


class EarthDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Earth
    pk_url_kwarg = 'pk'