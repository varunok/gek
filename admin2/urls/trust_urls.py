# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import trust_views

urlpatterns = [
    # trust
    url(
        '^trust/$',
        trust_views.TrustDetail.as_view(),
        name='trust'
    ),
    url(
        '^trust/gallery/$',
        trust_views.TrustGallery.as_view(),
        name='trust_gallery'
    ),
    url(
        '^trust/faq/$',
        trust_views.TrustFaq.as_view(),
        name='trust_faq'
    ),
    url(
        '^trust/feed/$',
        trust_views.TrustFeed.as_view(),
        name='trust_feed'
    ),
    url(
        '^trust/feed_video/$',
        trust_views.TrustFeedVideo.as_view(),
        name='trust_feed_video'
    ),
]