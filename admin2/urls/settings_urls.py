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
    url(
        r'^settings/franchise/$',
        settings_views.SettingFranchise.as_view(),
        name='settings_franchise'
    ),
    url(
        r'^settings/date-add/$',
        settings_views.SettingFranchiseAdd.as_view(),
        name='settings_franchise_add'
    ),
    url(
        r'^settings/privat24/$',
        settings_views.SettingsPrivate24View.as_view(),
        name='settings_private24'
    ),
    url(
        r'^settings/liqpay/$',
        settings_views.SettingsLiqpayView.as_view(),
        name='settings_liqpay'
    ),
    url(
        r'^settings/email-forward/$',
        settings_views.EmailForwardView.as_view(),
        name='email_forward'
    ),
    url(
        r'^settings/email-forward/create$',
        settings_views.EmailForwardCreate.as_view(),
        name='email_forward_create'
    ),
    url(
        r'^settings/email-forward/edit/(?P<pk>[\d-]+)/$',
        settings_views.EmailForwardEdit.as_view(),
        name='email_forward_edit'
    ),
    url(
        r'^settings/email-forward/delete/(?P<pk>[\d-]+)/$',
        settings_views.EmailForwardDelete.as_view(),
        name='email_forward_delete'
    ),
]