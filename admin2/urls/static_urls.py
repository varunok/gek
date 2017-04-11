# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import static_page_views

urlpatterns = [
    # STATIC PAGES
    url(
        r'^static_pages/$',
        static_page_views.StaticPageView.as_view(),
        name='static_pages'
    ),
    url(
        r'^static_pages/edit/(?P<slug>[\w-]+)/$',
        static_page_views.StaticPageDetailView.as_view(),
        name='static_page_detail'
    ),
    url(
        r'status_static_page',
        static_page_views.status_page,
        name='status_static_page'
    ),
]