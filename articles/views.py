# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView

from articles.models import Articles, Sections
from common.mixins import ViewsCountMixin
from seo.mixins import SEOMixin

PAGINATE_ARTICLE = 10


class ArticlesSiteView(SEOMixin, ListView):
    model = Articles
    context_object_name = 'objects'
    template_name = 'articles/articles.html'
    dinamic_template_name = 'articles/include/articles_list.html'
    # paginate_by = PAGINATE_ARTICLE

    def get_context_data(self, **kwargs):
        context = super(ArticlesSiteView, self).get_context_data(**kwargs)
        context['sections'] = Sections.objects.all().order_by('name')
        return context

    def get_queryset(self):
        self.object_list = Articles.objects.all()
        if self.request.GET.get('q'):
            self.object_list = self.object_list.filter(content__icontains=self.request.GET.get('q'))
        return self.object_list


class SectionsDetailView(SEOMixin, DetailView):
    model = Sections
    slug_field = 'slug'
    context_object_name = 'section'
    template_name = 'articles/sections.html'

    def get_context_data(self, **kwargs):
        context = super(SectionsDetailView, self).get_context_data(**kwargs)
        context['sections'] = Sections.objects.all().order_by('name')
        context['article_count'] = Articles.objects.count()
        context['articles'] = Articles.objects.filter(sections=self.object)
        if self.request.GET.get('q'):
            context['articles'] = context['articles'].filter(content__icontains=self.request.GET.get('q'))
        return context


class ArticlesDetailView(SEOMixin, ViewsCountMixin, DetailView):
    model = Articles
    slug_url_kwarg = 'slug_a'
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetailView, self).get_context_data(**kwargs)
        context['sections'] = Sections.objects.all().order_by('name')
        context['article_count'] = Articles.objects.count()
        return context
