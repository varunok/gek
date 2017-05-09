# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from admin2.forms import SectionUpdateForm, ArticlesUpdateForm
from articles.models import Sections, Articles
from common.mixins import MessageMixin, SuccesMixin


class SectionsView(LoginRequiredMixin, ListView):
    model = Sections
    context_object_name = 'sections'
    template_name = 'admin2/articles/sections_list.html'
    paginate_by = 10


class SectionsUpdateView(LoginRequiredMixin, SuccesMixin, UpdateView):
    model = Sections
    form_class = SectionUpdateForm
    template_name = 'admin2/articles/section_edit.html'


class SectionsDeleteView(LoginRequiredMixin, DeleteView):
    model = Sections
    template_name = 'admin2/common/delete_confirm.html'
    slug_field = 'slug'
    success_url = reverse_lazy('admin2:sections')


class SectionsCreateView(LoginRequiredMixin, SuccesMixin, MessageMixin, CreateView):
    model = Sections
    form_class = SectionUpdateForm
    template_name = 'admin2/articles/section_edit.html'


class ArticlesView(LoginRequiredMixin, ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'admin2/articles/articles_list.html'
    paginate_by = 10


class ArticlesUpdateView(LoginRequiredMixin, SuccesMixin, MessageMixin, UpdateView):
    model = Articles
    form_class = ArticlesUpdateForm
    context_object_name = 'article'
    template_name = 'admin2/articles/articles_edit.html'


class ArticlesCreateView(LoginRequiredMixin, SuccesMixin, MessageMixin, CreateView):
    model = Articles
    form_class = ArticlesUpdateForm
    template_name = 'admin2/articles/articles_edit.html'


class ArticlesDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    slug_field = 'slug'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:articles')