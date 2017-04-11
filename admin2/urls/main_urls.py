# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import main_views

urlpatterns = [
    # main view
    url('^$', main_views.Admin2MainView.as_view(), name='main'),
    url
        (
        '^app/dell/(?P<pk>\d+)/$',
        main_views.DellApplication.as_view(),
        name='dell_app'
    ),
    url(
        '^app/dell/all/$',
        main_views.DellAllAplications.as_view(),
        name='dell_app_all'
    ),
]