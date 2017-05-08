# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import settings_views

urlpatterns = [
# SETTINGS VIEW
    url(
        r'^settings/currency/$',
        settings_views.SettingsCurrencyView.as_view(),
        name='settings'
    ),
    url(
        r'^settings/site/$',
        settings_views.SettingsSite.as_view(),
        name='settings_site'
    ),
    url(
        r'^settings/address/$',
        settings_views.SettingsAddressView.as_view(),
        name='settings_address'
    ),
]