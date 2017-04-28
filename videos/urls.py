# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from videos.views import VideosList, VideosDetail

urlpatterns = [
    # video
    url('^$', VideosList.as_view(), name='video'),
    url('^(?P<pk>[\w-]+)/$', VideosDetail.as_view(), name='videos_detail'),
    ]