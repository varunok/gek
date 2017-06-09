# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import VideoServiceSet, BuildingEditForm
from admin2.helpers import BuildingFilterClass
from admin2.mixins import BuildingStatusMixin
from common.mixins import DeleteAjaxMixin, MessageMixin, SuccesMixin
from rieltor_object.models import Building


class BuildingListView(BuildingStatusMixin, ListView):
    model = Building
    template_name = 'admin2/rieltor_object/building/building_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = self.model.objects.order_by('point')
        if self.request.GET.get('search') == 'Поиск':
            qs = BuildingFilterClass(self.request, self.model).qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(BuildingListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Квартиры и Дома'
        context['create_url'] = reverse_lazy('admin2:building_create')
        return context


class BuildingEditView(SuccesMixin, MessageMixin, BuildingStatusMixin, UpdateView):
    model = Building
    template_name = 'admin2/rieltor_object/building/building_edit.html'
    success_url = reverse_lazy('admin2:buildings')
    form_class = BuildingEditForm

    def get_context_data(self, **kwargs):
        context = super(BuildingEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['verbose_name'] = self.model._meta.verbose_name
        return context


class BuildingCreateView(SuccesMixin, MessageMixin, BuildingStatusMixin, CreateView):
    model = Building
    form_class = BuildingEditForm
    template_name = 'admin2/rieltor_object/building/building_edit.html'


    def get_context_data(self, **kwargs):
        context = super(BuildingCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:buildings')
        return context


class BuildingDeleteView(BuildingStatusMixin, LoginRequiredMixin, DeleteView):
    model = Building
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:buildings')