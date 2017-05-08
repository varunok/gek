# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView

from landing.helpers import query_landing
from landing.models import Landing


class LandingPage(DetailView):
    model = Landing
    template_name = 'landing/multilending.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['object_list'] = query_landing(self.object)
        return context
