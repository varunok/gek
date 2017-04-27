# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from trust.views import Trust

urlpatterns = [
    # building
    url('^$', Trust.as_view(), name='trust'),
    ]