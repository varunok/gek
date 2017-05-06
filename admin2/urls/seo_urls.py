# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.seo_views import SEOList, SeoCreate, SEOEdit, SeoDelete

urlpatterns = [
    # SEO
    url(
        r'^seo/$',
        SEOList.as_view(),
        name='seo'
    ),
    url(
        r'^seo/delete/(?P<pk>[\w-]+)/$',
        SeoDelete.as_view(),
        name='seo_delete'
    ),
    url(
        r'^seo/edit/(?P<pk>[\w-]+)/$',
        SEOEdit.as_view(),
        name='seo_edit'
    ),
    url(
        r'^seo/create/$',
        SeoCreate.as_view(),
        name='seo_create'
    ),
]