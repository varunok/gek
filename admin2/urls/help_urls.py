# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.help_views import HelpWatchView, HelpListEditView, HelpEdit, HelpCreate, HelpDelete

urlpatterns = [
    # Help
    url(
        '^helps_watch/$',
        HelpWatchView.as_view(),
        name='helps_watch'
    ),
    url(
        '^helps_list/$',
        HelpListEditView.as_view(),
        name='helps_list'
    ),
    url(
        '^helps/edit/(?P<pk>[\d-]+)/$',
        HelpEdit.as_view(),
        name='help_edit'
    ),
    url(
        '^helps/delete/(?P<pk>[\d-]+)/$',
        HelpDelete.as_view(),
        name='help_delete'
    ),
    url(
        '^helps/create/$',
        HelpCreate.as_view(),
        name='help_create'
    ),
]