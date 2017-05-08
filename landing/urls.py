# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from landing.views import LandingPage

urlpatterns = [
    # landing
    url(r'^(?P<slug>[\w-]+)', LandingPage.as_view(), name='landing'),
]