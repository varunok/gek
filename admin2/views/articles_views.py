# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from admin2.form import SectionUpdateForm
from articles.models import Sections
from common.views import DeleteAjaxMixin


class SectionsView(LoginRequiredMixin, ListView):
    model = Sections
    # slug_field = 'slug'
    context_object_name = 'sections'
    template_name = 'admin2/articles/sections_list.html'


class SectionsDetailView(LoginRequiredMixin, DetailView):
    model = Sections
    slug_field = 'slug'
    context_object_name = 'section'
    template_name = 'admin2/test2.html'


class SectionsUpdateView(LoginRequiredMixin, UpdateView):
    model = Sections
    form_class = SectionUpdateForm
    template_name = 'admin2/articles/section_edit.html'
    success_url = reverse_lazy('admin2:sections')


class SectionsDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Sections
    slug_field = 'slug'


class SectionsCreateView(LoginRequiredMixin, CreateView):
    model = Sections
    form_class = SectionUpdateForm
    template_name = 'admin2/articles/section_edit.html'
    success_url = reverse_lazy('admin2:sections')

