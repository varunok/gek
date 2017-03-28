# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from articles.views import ArticlesDetailView, SectionsDetailView, ArticlesSiteView

urlpatterns = [
    url('^$', ArticlesSiteView.as_view(), name='articles'),
    url('more_pages$', ArticlesSiteView.as_view(), name='more_pages'),

    url(
        '^(?P<slug>[\w-]+)$',
        SectionsDetailView.as_view(),
        name='sections_detail'
    ),
    url(
        '^(?P<slug_s>[\w-]+)/(?P<slug_a>[\w-]+)$',
        ArticlesDetailView.as_view(),
        name='article_detail'
    ),
]