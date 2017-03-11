# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import login_views, main_views, articles_views

urlpatterns = [
    # login views
    url('^login/$', login_views.LoginRememberView.as_view(), name='auth_login'),

    # main view
    url('^$', main_views.Admin2MainView.as_view(), name='main'),
    url
    (
        '^app/dell/(?P<pk>\d+)/$',
        main_views.DellApplication.as_view(),
        name='dell_app'
    ),
    url(
        '^app/dell/all/$',
        main_views.DellAllAplications.as_view(),
        name='dell_app_all'
    ),
    # main articles
    url(
        '^articles/sections/$',
        articles_views.SectionsView.as_view(),
        name='sections'
    ),
    url(
        '^articles/sections/(?P<slug>[\w-]+)$',
        articles_views.SectionsDetailView.as_view(),
        name='sections_detail'
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
]