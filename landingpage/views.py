# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import shuffle

from django.shortcuts import render
from django.views.generic import TemplateView

from admin2.models import IndexPageModel, TrustPageModel, SettingsAddress
from landingpage.forms import LandingForms
from rieltor_object.filters import FilterDaily, FilterBuilding, FilterOfise
from rieltor_object.helpers import HelperFilter
from rieltor_object.models import Ofice, Building, Daily
from common.mixins import DinamicPageMixin
from seo.mixins import SEOMixin
from services.models import ServicesRieltor


class Superlending(SEOMixin, DinamicPageMixin, TemplateView):
    template_name = 'superlending.html'
    dinamic_template_name = 'include/item.html'
    paginate_by = 9
    queryFilter = None

    def get_context_data(self, **kwargs):
        context = super(Superlending, self).get_context_data(**kwargs)
        self.queryFilter = queryFilter = HelperFilter(self.request).qd
        context['indexpagemodel'] = IndexPageModel.get_solo()
        context['service_rieltor'] = ServicesRieltor.get_solo()
        context['trust'] = TrustPageModel.get_solo()
        context['city_plural'] = SettingsAddress.get_solo().city_plural
        context['BASE_URL'] = '/search'
        if queryFilter:
            buildings = list(FilterBuilding(queryFilter,
                                            queryset=Building.objects.all()).qs)
            offices = list(FilterOfise(queryFilter,
                                       queryset=Ofice.objects.all()).qs)
            daily = list(FilterDaily(queryFilter,
                                     queryset=Daily.objects.all()).qs)
            context['filter_results'] = buildings+daily+offices
            context['filtering'] = True
            context['form'] = LandingForms(queryFilter)
        else:
            context['results'] = self.get_queryset()
            context['form'] = LandingForms()
        try:
            context['faqs'] = ServicesRieltor.get_solo().fag.all().order_by('id')
        except AttributeError:
            pass
        return context

    def get_queryset(self):
        offices = list(Ofice.objects.all())
        buildings = list(Building.objects.all())
        daily = list(Daily.objects.all())
        result = buildings+daily+offices
        return result


class SuperlendingInner(TemplateView):
    template_name = 'superlending_inner.html'
