# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.redirect_views import RedrectList, RedirectCreate, RedirectEdit, RedirectDelete

urlpatterns = [
    # Redirect
    url(
        r'^redirects/$',
        RedrectList.as_view(),
        name='redirects'
    ),
    url(
        r'^redirects/create/$',
        RedirectCreate.as_view(),
        name='redirect_create'
    ),
    url(
        r'^redirects/edit/(?P<pk>[\w-]+)/$',
        RedirectEdit.as_view(),
        name='redirect_edit'
    ),
    url(
        r'^redirects/delete/(?P<pk>[\w-]+)/$',
        RedirectDelete.as_view(),
        name='redirect_delete'
    ),
]