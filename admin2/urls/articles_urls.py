# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import articles_views

urlpatterns = [
    # sections article, articles_view
    url(
        '^articles/sections/$',
        articles_views.SectionsView.as_view(),
        name='sections'
    ),
    url(
        '^articles/sections/update/(?P<slug>[\w-]+)/$',
        articles_views.SectionsUpdateView.as_view(),
        name='sections_update'
    ),
    url(
        '^articles/sections/delete/(?P<slug>[\w-]+)/$',
        articles_views.SectionsDeleteView.as_view(),
        name='sections_delete'
    ),
    url(
        '^articles/sections/create/$',
        articles_views.SectionsCreateView.as_view(),
        name='sections_create'
    ),

    # articles, articles_view
    url(
        '^articles/articles/$',
        articles_views.ArticlesView.as_view(),
        name='articles'
    ),
    url(
        '^articles/articles/update/(?P<slug>[\w-]+)/$',
        articles_views.ArticlesUpdateView.as_view(),
        name='articles_update'
    ),
    url(
        '^articles/articles/create/$',
        articles_views.ArticlesCreateView.as_view(),
        name='articles_create'
    ),
    url(
        '^articles/articles/delete/(?P<slug>[\w-]+)/$',
        articles_views.ArticlesDeleteView.as_view(),
        name='articles_delete'
    ),
]