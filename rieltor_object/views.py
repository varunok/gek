# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView, FormView, TemplateView

from common.mixins import ViewsCountMixin, DinamicNextMixin
from rieltor_object.forms import FilterForm
from rieltor_object.models import Building, TypeDeal
from rieltor_object.search import BuildingFilter


PAGINATE_OBJ = 10

class BuildingListSiteView(DinamicNextMixin, ListView):
    model = Building
    template_name = 'rieltor_object/building_list.html'
    paginate_by = PAGINATE_OBJ

    def get_context_data(self, **kwargs):
        context = super(BuildingListSiteView, self).get_context_data(**kwargs)
        context['filter_form'] = FilterForm()
        return context


class BuildingDetailSiteView(ViewsCountMixin, DetailView):
    model = Building
    template_name = 'rieltor_object/building.html'


@require_http_methods(["POST"])
def searchbuildingview(request):
    if request.method == 'POST':
        template_name = 'rieltor_object/include/building_item.html'
        f = BuildingFilter(request.POST, queryset=Building.objects.all())
        return render(request, template_name, {'objects': f.qs})
    return HttpResponse(status=404)


class SearchBuildView(DinamicNextMixin, ListView):
    paginate_by = PAGINATE_OBJ
    model = Building
    template_name = 'rieltor_object/include/building_item.html'
    dinamic_template_name = 'rieltor_object/include/building_item.html'

    def get_queryset(self):
        return BuildingFilter(self.request.POST, queryset=self.model.objects.all()).qs