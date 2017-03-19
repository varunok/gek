# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from admin2.form import SectionUpdateForm, ArticlesUpdateForm
from articles.models import Sections, Articles
from common.mixins import DeleteAjaxMixin


class SectionsView(LoginRequiredMixin, ListView):
    model = Sections
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


class ArticlesView(LoginRequiredMixin, ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'admin2/articles/articles_list.html'


class ArticlesDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    slug_field = 'slug'
    context_object_name = 'article'
    template_name = 'admin2/test2.html'


class ArticlesUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    form_class = ArticlesUpdateForm
    context_object_name = 'article'
    template_name = 'admin2/articles/articles_edit.html'
    success_url = reverse_lazy('admin2:articles')


class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = ArticlesUpdateForm
    template_name = 'admin2/articles/articles_edit.html'
    success_url = reverse_lazy('admin2:articles')


class ArticlesDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Articles
    slug_field = 'slug'