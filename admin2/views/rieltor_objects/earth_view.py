# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import EarthEditForm
from admin2.helpers import BuildingFilterClass
from admin2.mixins import EarthStatusMixin
from common.mixins import DeleteAjaxMixin, SuccesMixin, MessageMixin
from rieltor_object.models import Earth, EarthDistrict


class EarthListView(EarthStatusMixin, ListView):
    model = Earth
    template_name = 'admin2/rieltor_object/earth/earth_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.request.GET.get('search') == 'Поиск':
            qs = BuildingFilterClass(self.request, self.model).qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(EarthListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Земля'
        context['create_url'] = reverse_lazy('admin2:earth_create')
        context['districts'] = EarthDistrict.objects.all()
        return context


class EarthEditView(SuccesMixin, MessageMixin, EarthStatusMixin, UpdateView):
    model = Earth
    template_name = 'admin2/rieltor_object/earth/earth_edit.html'
    form_class = EarthEditForm

    def get_context_data(self, **kwargs):
        context = super(EarthEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['verbose_name'] = self.model._meta.verbose_name
        return context


class EarthCreateView(SuccesMixin, MessageMixin, EarthStatusMixin, CreateView):
    model = Earth
    form_class = EarthEditForm
    template_name = 'admin2/rieltor_object/earth/earth_edit.html'

    def get_context_data(self, **kwargs):
        context = super(EarthCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:earth')
        return context


class EarthDeleteView(LoginRequiredMixin, DeleteView):
    model = Earth
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:earth')