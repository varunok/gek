# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from landing.views import redirect_view

urlpatterns = [
    # landing
    url(r'^(?P<slug>[\w-]+)', redirect_view, name='landing'),
]