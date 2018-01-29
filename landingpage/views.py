# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import shuffle

from django.shortcuts import render
from django.views.generic import TemplateView

from admin2.models import IndexPageModel, TrustPageModel, SettingsAddress
from rieltor_object.models import Ofice, Building, Daily
from common.mixins import DinamicPageMixin
from seo.mixins import SEOMixin
from services.models import ServicesRieltor


class Superlending(SEOMixin, DinamicPageMixin, TemplateView):
    template_name = 'superlending.html'
    dinamic_template_name = 'include/item.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(Superlending, self).get_context_data(**kwargs)
        context['results'] = self.get_queryset()
        context['indexpagemodel'] = IndexPageModel.get_solo()
        context['service_rieltor'] = ServicesRieltor.get_solo()
        context['trust'] = TrustPageModel.get_solo()
        context['city_plural'] = SettingsAddress.get_solo().city_plural
        try:
            context['faqs'] = ServicesRieltor.get_solo().fag.all().order_by('id')
        except AttributeError:
            pass
        return context

    @staticmethod
    def get_queryset():
        offices = list(Ofice.objects.all())
        buildings = list(Building.objects.all())
        daily = list(Daily.objects.all())
        result = buildings+daily+offices
        # shuffle(result)
        return result

