# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import VideoServiceSet, BuildingEditForm, NewBuildingEditForm
from admin2.helpers import BuildingFilterClass
from admin2.mixins import NewBuildingStatusMixin
from common.mixins import DeleteAjaxMixin, SuccesMixin, MessageMixin
from rieltor_object.models import NewBuilding, Building, Infrastructure, Accommodations, District


class NewBuildingListView(NewBuildingStatusMixin, ListView):
    model = NewBuilding
    template_name = 'admin2/rieltor_object/new_building/new_building_list.html'
    paginate_by = 10
    ordering = ['point']

    def get_queryset(self):
        qs = self.model.objects.order_by('point')
        if self.request.GET.get('search') == 'Поиск':
            qs = BuildingFilterClass(self.request, self.model).qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(NewBuildingListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Новострои'
        context['create_url'] = reverse_lazy('admin2:newbuilding_create')
        context['districts'] = District.objects.all()
        return context


class NewBuildingEditView(SuccesMixin, MessageMixin, NewBuildingStatusMixin, UpdateView):
    model = NewBuilding
    template_name = 'admin2/rieltor_object/new_building/new_building_edit.html'
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


class NewBuildingCreateView(SuccesMixin, MessageMixin, NewBuildingStatusMixin, CreateView):
    model = NewBuilding
    form_class = NewBuildingEditForm
    template_name = 'admin2/rieltor_object/new_building/new_building_edit.html'

    def get_context_data(self, **kwargs):
        context = super(NewBuildingCreateView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['list_url'] = reverse_lazy('admin2:newbuildings')
        return context


class NewBuildingDeleteView(LoginRequiredMixin, DeleteView):
    model = NewBuilding
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:newbuildings')


def related_building(request, object_id, building_id):
    newbuilding_set = NewBuilding.objects.filter(id=object_id, building=building_id)
    building = Building.objects.get(id=building_id)
    newbuilding = NewBuilding.objects.get(id=object_id)
    print(newbuilding.building.all())
    if newbuilding_set:
        newbuilding.building.remove(building)
        return HttpResponse(status=200, content='Удалено')
    building.newbuilding = newbuilding
    building.save()
    return HttpResponse(status=200, content='Добавлено')