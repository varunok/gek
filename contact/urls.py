# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from contact.views import Contacts

urlpatterns = [
    # building
    url('^$', Contacts.as_view(), name='contact'),
    ]