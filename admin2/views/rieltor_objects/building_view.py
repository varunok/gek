# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from admin2.forms import VideoServiceSet, BuildingEditForm
from rieltor_object.models import Building


class BuildingListView(ListView):
    model = Building
    template_name = 'admin2/rieltor_object/building/building_list.html'

    def get_context_data(self, **kwargs):
        context = super(BuildingListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Квартиры и Дома'
        context['create_url'] = reverse_lazy('admin2:building_create')
        return context

class BuildingEditView(UpdateView):
    model = Building
    template_name = 'admin2/rieltor_object/building/building_edit.html'
    success_url = reverse_lazy('admin2:buildings')
    form_class = BuildingEditForm
    video_form = VideoServiceSet

    def get_context_data(self, **kwargs):
        context = super(BuildingEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['video_form'] = self.video_form(instance=self.get_object())
        context['video_check'] = self.get_object().videos.all().order_by('id')
        context['verbose_name'] = self.model._meta.verbose_name
        return context


class BuildingCreateView(CreateView):
    model = Building
    form_class = BuildingEditForm
    template_name = 'admin2/rieltor_object/building/building_edit.html'


    def get_context_data(self, **kwargs):
        context = super(BuildingCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:buildings')
        return context

    def get_success_url(self):
        return self.object.get_edit_url()