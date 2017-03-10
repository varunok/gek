# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView

from articles.models import Sections


class SectionsView(LoginRequiredMixin, ListView):
    model = Sections
    # slug_field = 'slug'
    context_object_name = 'sections'
    template_name = 'admin2/sections_list.html'


class SectionsDetailView(LoginRequiredMixin, DetailView):
    model = Sections
    slug_field = 'slug'
    context_object_name = 'section'
    template_name = 'admin2/test2.html'