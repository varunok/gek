# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import videos_views

urlpatterns = [
    # trust
    url(
        '^video/$',
        videos_views.VideosList.as_view(),
        name='videos'
    ),
    url(
        '^video/edit/(?P<pk>[\w-]+)/$',
        videos_views.VideosEdit.as_view(),
        name='videos_edit'
    ),
    url(
        '^video/create/$',
        videos_views.VideosCreate.as_view(),
        name='videos_create'
    ),
    url(
        '^video/edit/you_knows/(?P<pk>[\w-]+)/$',
        videos_views.VideosKnowsEdit.as_view(),
        name='videos_edit_knows'
    ),
    url(
        '^video/delete/(?P<pk>[\w-]+)/$',
        videos_views.VideosDeleteView.as_view(),
        name='videos_delete'
    ),
]