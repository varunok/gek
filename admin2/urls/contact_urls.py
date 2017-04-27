# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import contact_views

urlpatterns = [
    # contact
    url(
        '^contact/$',
        contact_views.ContactUpdate.as_view(),
        name='contact'
    ),
    url(
        '^contact/schedule/$',
        contact_views.ContactSchedule.as_view(),
        name='contact_schedule'
    ),
    ]