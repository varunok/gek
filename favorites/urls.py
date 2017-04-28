# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from favorites.views import FavoritesPage, set_favorites

urlpatterns = [
    # favorites
    url('^$', FavoritesPage.as_view(), name='favorites'),
    url('^set/(?P<content_type>[\w-]+)/(?P<object_id>[\w-]+)$', set_favorites, name='set_favorites'),
    url('^favorites/set/(?P<content_type>[\w-]+)/(?P<object_id>[\w-]+)$', set_favorites, name='set_favorites'),
    # url('set/^(?P<pk>[\w-]+)/$', VideosDetail.as_view(), name='videos_detail'),
    ]