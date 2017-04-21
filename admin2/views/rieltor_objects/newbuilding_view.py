# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import VideoServiceSet, BuildingEditForm, NewBuildingEditForm
from common.mixins import DeleteAjaxMixin
from rieltor_object.models import NewBuilding, Building, Infrastructure, Accommodations


class NewBuildingListView(ListView):
    model = NewBuilding
    template_name = 'admin2/rieltor_object/new_building/new_building_list.html'

    def get_context_data(self, **kwargs):
        context = super(NewBuildingListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Новострои'
        context['create_url'] = reverse_lazy('admin2:building_create')
        return context


class NewBuildingEditView(UpdateView):
    model = NewBuilding
    template_name = 'admin2/rieltor_object/new_building/new_building_edit.html'
    success_url = reverse_lazy('admin2:newbuildings')
    form_class = NewBuildingEditForm
    video_form = VideoServiceSet

    def get_context_data(self, **kwargs):
        context = super(NewBuildingEditView, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['video_form'] = self.video_form(instance=self.get_object())
        context['video_check'] = self.get_object().videos.all().order_by('id')
        context['verbose_name'] = self.model._meta.verbose_name
        context['buildings'] = Building.objects.exclude(newbuilding=self.object)
        context['infrastructures'] = Infrastructure.objects.exclude(newbuilding=self.object)
        context['accommodations'] = Accommodations.objects.exclude(newbuilding=self.object)
        return context


def related_building(request, object_id, building_id):
    newbuilding_set = NewBuilding.objects.filter(building=building_id)
    building = Building.objects.get(id=building_id)
    newbuilding = NewBuilding.objects.get(id=object_id)
    if newbuilding_set:
        newbuilding.building.remove(building)
        return HttpResponse(status=200, content='Удалено')
    building.newbuilding = newbuilding
    building.save()
    return HttpResponse(status=200, content='Добавлено')

# class BuildingCreateView(CreateView):
#     model = Building
#     form_class = BuildingEditForm
#     template_name = 'admin2/rieltor_object/building/building_edit.html'
#
#
#     def get_context_data(self, **kwargs):
#         context = super(BuildingCreateView, self).get_context_data(**kwargs)
#         context['verbose_name'] = self.model._meta.verbose_name
#         context['list_url'] = reverse_lazy('admin2:buildings')
#         return context
#
#     def get_success_url(self):
#         return self.object.get_edit_url()
#
#
# class BuildingDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
#     model = Building
#     pk_url_kwarg = 'pk'