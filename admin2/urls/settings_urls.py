# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import settings_views

urlpatterns = [
# SETTINGS VIEW
    url(
        r'^settings/$',
        settings_views.SettingsView.as_view(),
        name='settings'
    ),
]